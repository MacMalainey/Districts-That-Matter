import os
import numpy as np
import shapely
import spatialite
from libpysal.weights import Queen, KNN
import pandas as pd
import geopandas as gpd
import queries
import matplotlib.pyplot as plt
import json
from sklearn.cluster import AgglomerativeClustering

""" Get data from database and create pandas frame"""
print("Loading and Processing Data...")
db = spatialite.connect(
            os.path.dirname(__file__) + "/../.local/dtmTORO.db"
        )

query = "SELECT *, AsText(bd.geometry) AS geometry_wkt FROM census_data AS cd, boundary_data AS bd USING (dguid);"

pd_df = pd.read_sql(query,db)
#TODO: make dguid as the index column and make downstream changes
#TODO: ask Mac to add query to queries.py

""" Process data to get percentages"""
with open(os.path.dirname(__file__) + "/../.local/dtmTORO_schema.json", 'r') as schema_file:
    schema = json.load(schema_file)

for col_name in schema["ages"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_ages"] * 100

for col_name in schema["marital_status"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_marital_status"]  * 100

for col_name in schema["household"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_household"]  * 100

for col_name in schema["income"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_income"]  * 100

for col_name in schema["immigrated"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_immigrated"]  * 100

for col_name in schema["birthplace"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_birthplace"]  * 100

for col_name in schema["generation"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_generation"]  * 100

for col_name in schema["visible_minority"]:
    pd_df[col_name] = pd_df[col_name] / (pd_df["rc_visible_minority"] + pd_df["visible_minority_not_applicable"])  * 100

#TODO: ask Mac to modify database

# The column names below is the only one where inf values are possible if rc (for visible minoirties) = 0 yet there are still
# those who are not visible minorities
#pd_df['visible_minority_not_applicable'] = pd_df['visible_minority_not_applicable'].replace([float('inf'), float('-inf')], 100)


""" Create geopandas dataframe and contiguiuty weights matrix """

pd_df['geometry'] = pd_df['geometry_wkt'].apply(lambda x: shapely.from_wkt(x))
pd_df.drop(columns=["geometry_wkt"])

gpd_df = gpd.GeoDataFrame(pd_df, crs="EPSG:4326", geometry="geometry")

print("Building a contiguity matrix...")
queen_contiguity_weights = Queen.from_dataframe(gpd_df, use_index=True)
knn_contiguity_weights = KNN.from_dataframe(gpd_df, k=4)

""" Clustering """
print("Clustering to form COIs...")
# Set seed for reproducibility
np.random.seed(0)
# Initialize the algorithm
model = AgglomerativeClustering(linkage="ward", n_clusters=10, connectivity=knn_contiguity_weights.sparse, compute_distances=True)
# Fill in null values
clustering_relevant_cols = schema["ages"] + schema["marital_status"] + schema["household"] + schema["income"] + schema["immigrated"] + schema["birthplace"] + schema["generation"] + schema["visible_minority"]
df_cluster_cols = gpd_df[clustering_relevant_cols]
df_filled = df_cluster_cols.fillna(df_cluster_cols.mean())
# Run clustering
model.fit(df_filled)
# Assign labels to main data table
gpd_df["COI"] = model.labels_

# Visualize Results 
gpd_df.plot(
    column="COI",
    categorical=True,
    cmap="Set3",
    legend=True,
    linewidth=0,
)

plt.savefig('plot.png')

sizes = gpd_df.groupby("COI").size()
poplation_totals = gpd_df.groupby("COI")["population"].sum()
merged_summary = pd.concat([sizes, poplation_totals], axis=1)
print(merged_summary)

""" Explaining COI creation"""
print("Generating Explanation for formed COIs...")

def aggregate_to_list(series):
    return list(series)

COI_col_aggfuncs = {}
for col in clustering_relevant_cols:
    COI_col_aggfuncs[col] = 'mean'
COI_col_aggfuncs |= {'dguid': aggregate_to_list, 'population': 'sum', 'landarea': 'sum', 
                                                 'rc_ages': 'sum', 'rc_marital_status': 'sum', 'rc_household': 'sum',
                                                  'rc_income': 'sum', 'rc_immigrated': 'sum', 'rc_birthplace': 'sum', 
                                                  'rc_generation': 'sum', 'rc_visible_minority': 'sum', 
                                                  'landarea': 'mean', 'density': 'mean' }
clusters_df = gpd_df.dissolve(by='COI', aggfunc=COI_col_aggfuncs)
#TODO: Ask Harsh if this data for the COIs is what he needs

COI_neighbor_weight_matrix = Queen.from_dataframe(clusters_df, use_index=True)

clusters_df['explanation'] = pd.Series([None] * len(clusters_df))
bad_expl_count = 0
for index, row in clusters_df.iterrows():
    neighbor_indices = list(COI_neighbor_weight_matrix[index].keys())
    neighbor_rows = clusters_df.iloc[neighbor_indices]
    neighbor_rows = neighbor_rows[clustering_relevant_cols]
    neighbor_means = neighbor_rows.mean()
    neighbor_pop_mean = clusters_df.loc[neighbor_indices, 'population'].mean()
    neighbor_vars = neighbor_rows.std()
    z_scores = pd.Series(dtype=float)
    for col in clustering_relevant_cols:
        #if neighbor_vars[col] ==0 or pd.isna(neighbor_vars[col]):
        neighbor_vars[col] = 5 #set 20% difference to be one standard deviation
        z_scores[col] = (row[col] - neighbor_means[col]) / neighbor_vars[col]
    z_scores_abs = z_scores.abs()
    large_z_scores =  z_scores_abs[z_scores_abs > 2] 
    largest_z_scores =  z_scores_abs.nlargest(5, keep='all')  #z_scores_abs[z_scores_abs > 2.5] #
    explaination_dict = {}
    #print(f"largest_z_scores: {largest_z_scores} for index {index}")
    for attribute in large_z_scores.index:
        #print(f"attr: {attribute}")
        explaination_dict[attribute] = {'z-score': z_scores[attribute], 'my_val': row[attribute], 
                                        'neighbor-mean': neighbor_means[attribute],
                                        'neighbor-var': neighbor_vars[attribute], 
                                        'neighbor_vals': neighbor_rows[attribute].to_list()}
    clusters_df.at[index, 'explanation'] = explaination_dict
    if (large_z_scores.count() < 2):
            print(f"For COI {index}, explnation {explaination_dict}")
            bad_expl_count +=1
#TODO: Think about how to modify clustering to avoid conflicting columns from being clustered
#TODO: Investigate and Drop explanation attributes where z-score is too low
#TODO: Change clustering alg to not look at std var in distance but rather have 5% as variation

print(f"bad_expl_count: {bad_expl_count}")

"""Code Snippets for Debugging"""

# means = gpd_df.groupby("COI")[clustering_relevant_cols].mean()
# means.to_csv("means.csv")


# ------
# plt.title("Hierarchical Clustering Dendrogram")
# # plot the top three levels of the dendrogram
# plot_dendrogram(model, truncate_mode="level", p=10)
# plt.xlabel("Number of points in node (or index of point if no parenthesis).")
# plt.savefig("dendogram.png")

# ---------

#contiguity_weights.plot(gpd_df)

#plt.savefig('plot2.png')

# plt.switch_backend("TkAgg")
# --------------
# def count_zeros(df, column_name):
#     return len(df[df[column_name] == 0])

# def count_nan(df, column_name):
#     return df[column_name].isna().sum()

# def count_infinities(df, column_name):
#     return (df[column_name] == float('inf')).sum()
# ---------------------
# for i in  [153,273,303,350,728,793,1477,1501,1877,2206,2247,2673,3054,3688,3898,3992]:
#     print(i)
#     print(pd_df.loc[i,"visible_minority_not_applicable"])
#     print(pd_df.loc[i, "rc_visible_minority"])
#     print(pd_df.loc[i,"visible_minority_not_applicable"] / pd_df.loc[i, "rc_visible_minority"]  * 100)
#     print()
# -------
# pd_df["orig_visible_miniority_na"] = pd_df["visible_minority_not_applicable"].copy()

# ------------
# gpd_df.plot(
#         column="ages_0_to_4",
#         scheme="natural_breaks",
#         linewidth=0,
#         cmap="RdPu",
#         legend=True,
# )

# plt.savefig('plot.png')

# gpd_df.plot(
#         column="population",
#         scheme="natural_breaks",
#         linewidth=0,
#         cmap="RdPu",
#         legend=True,
# )

# plt.savefig('plot2.png')
# -----------------
# for index,row in gpd_df.iterrows():
#     neighbor_indices = contiguity_weights.neighbors[index]
#     for col in gpd_df.columns:
#         if pd.isna(row[col]):
#             neighbor_vals = [gpd_df.loc(i, col) for i in neighbor_indices]
#             neighbor_indices.drop

#     mean_value = gdf['column_name'].mean()
#     gdf['column_name'] = gdf['column_name'].fillna(mean_value)


# print(contiguity_weights.neighbors[0])
