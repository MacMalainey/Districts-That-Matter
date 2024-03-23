from collections import OrderedDict
import os
import numpy as np
import shapely
from sklearn.metrics import silhouette_score
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

# midpoints = {
#     "income_under_5k": 2.5,
#     "income_from_5k_to_10k": 7.5,
#     "income_from_10k_to_10k": 12.5,
#     "income_from_15k_to_20k": 17.5,
#     "income_from_20k_to_25k": 22.5,
#     "income_from_25k_to_30k": 27.5,
#     "income_from_30k_to_35k": 32.5,
#     "income_from_35k_to_40k": 37.5,
#     "income_from_40k_to_45k": 42.5,
#     "income_from_45k_to_50k": 27.5,
#     "income_from_50k_to_60k": 55,
#     "income_from_60k_to_70k": 65,
#     "income_from_70k_to_80k": 75,
#     "income_from_80k_to_90k": 85,
#     "income_from_90k_to_100k": 95,
#     "income_income_from_100k_to_125k": 112.5,
#     "income_income_from_125k_to_150k": 137.5,
#     "income_income_from_150k_to_200k": 175,
#     "income_income_from_200k_and_over": 300,
#     "ages_0_to_4": 2,
#     "ages_5_to_9": 7,
#     "ages_10_to_14": 12,
#     "ages_15_to_19": 17,
#     "ages_20_to_24": 22,
#     "ages_25_to_29": 27,
#     "ages_30_to_34": 32,
#     "ages_35_to_39": 37,
#     "ages_40_to_44": 42,
#     "ages_45_to_49": 47,
#     "ages_50_to_54": 52,
#     "ages_55_to_59": 57,
#     "ages_60_to_64": 62,
#     "ages_65_to_69": 67,
#     "ages_70_to_74": 72,
#     "ages_75_to_79": 77,
#     "ages_80_to_84": 83,
#     "ages_85_and_over": 90,
# }

""" Process data to get percentages"""
with open(os.path.dirname(__file__) + "/../.local/dtmTORO_schema.json", 'r') as schema_file:
    schema = json.load(schema_file)

# pd_df['avg_income'] = pd.Series([0.0] * pd_df.shape[0])
# pd_df['avg_age'] = pd.Series([0.0] * pd_df.shape[0])


for col_name in schema["ages"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_ages"] * 100
    # pd_df['avg_age'] = pd_df[col_name] * midpoints[col_name]


for col_name in schema["marital_status"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_marital_status"]  * 100

for col_name in schema["household"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_household"]  * 100

for col_name in schema["income"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_income"]  * 100
    # pd_df['avg_income'] = pd_df[col_name] * midpoints[col_name]

for col_name in schema["immigrated"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_immigrated"]  * 100

for col_name in schema["birthplace"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_birthplace"]  * 100

for col_name in schema["generation"]:
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_generation"]  * 100

for col_name in schema["visible_minority"]:
    pd_df[col_name] = pd_df[col_name] / (pd_df["rc_visible_minority"] + pd_df["visible_minority_not_applicable"])  * 100

# min_value = pd_df["avg_income"].min()
# max_value = pd_df["avg_income"].max()
# pd_df["avg_income"] = (pd_df["avg_income"] - min_value) / (max_value - min_value) * 100

# min_value = pd_df["avg_age"].min()
# max_value = pd_df["avg_age"].max()
# pd_df["avg_age"] = (pd_df["avg_age"] - min_value) / (max_value - min_value) * 100
#TODO: ask Mac if we should modify database for visible minorities; and add language or other deatures

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
# Fill in null values for clustering
clustering_relevant_cols = schema["ages"] + schema["marital_status"] + schema["household"] + schema["income"] + schema["immigrated"] + schema["birthplace"] + schema["generation"] + schema["visible_minority"]
df_cluster_cols = gpd_df[clustering_relevant_cols]
df_filled = df_cluster_cols.fillna(df_cluster_cols.mean())


print("Clustering to form COIs...")
# Set seed for reproducibility
np.random.seed(0)

# k_list = list(range(2, 51, 2))
# silhouette_scores = []
# for k in k_list:
#     # Initialize the algorithm
#     model = AgglomerativeClustering(linkage="ward", n_clusters=k, connectivity=knn_contiguity_weights.sparse, compute_distances=True)
#     # Run clustering
#     model.fit(df_filled)
#     labels = model.labels_
#     silhouette_scores.append(silhouette_score(df_filled, labels))

# plt.plot(k_list, silhouette_scores, marker='o')
# plt.xlabel('Number of clusters')
# plt.ylabel('Silhoette_Score')
# plt.title('Elbow Method for Agglomerative Clustering')
# plt.xticks(k_list)
# plt.grid(True)
# plt.savefig('elbow.png')

#Initialize the algorithm
model = AgglomerativeClustering(linkage="ward", n_clusters=10, connectivity=knn_contiguity_weights.sparse, compute_distances=True)
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
        if neighbor_vars[col] == 0 or pd.isna(neighbor_vars[col]) or neighbor_vars[col] < 5:
            neighbor_vars[col] = 5 #set 5% difference to be minimum one standard deviation
        z_scores[col] = (row[col] - neighbor_means[col]) / neighbor_vars[col]
    z_scores_abs = z_scores.abs()
    large_abs_z_scores =  (z_scores_abs[z_scores_abs > 2])
    if large_abs_z_scores.count() == 0:
        bad_expl_count+=1
    if (large_abs_z_scores.count() <=1):      
        largEST_abs_z_scores =  z_scores_abs.nlargest(2, keep='all')
        large_abs_z_scores = large_abs_z_scores.combine_first(largEST_abs_z_scores)

    # # Selecting a subset of clusters (e.g., clusters 2 and 3)
    # subset_cluster_indices = [index,] + neighbor_indices
    # subset_data_row_indices= [i for i, data_row in gpd_df.iterrows() if data_row['COI'] in subset_cluster_indices]
    # data_subset = df_filled.loc[subset_data_row_indices]

    # # Calculate silhouette scores for the subset of clusters
    # sil_score = silhouette_score(data_subset, gpd_df.loc[subset_data_row_indices,"COI"])
    # print(f"Index {index}, sil score: {sil_score} ")
    # explaination_dict = {'sil_score': sil_score}
    explaination_dict = OrderedDict()
    large_abs_z_scores.sort_values(ascending=False, inplace=True)
    #print(f"largest_z_scores: {largest_z_scores} for index {index}")
    for attribute in large_abs_z_scores.index:
        #print(f"attr: {attribute}")
        explaination_dict[attribute] = {'z_score': z_scores[attribute], 'my_val': row[attribute], 
                                        'neighbor_mean': neighbor_means[attribute],
                                        'neighbor_var': neighbor_vars[attribute], 
                                        'neighbor_vals': neighbor_rows[attribute].to_list()}
    clusters_df.at[index, 'explanation'] = explaination_dict
    # if (large_abs_z_scores.count() == 0):
    #         print(f"For COI {index}, explnation {explaination_dict}")
    #         bad_expl_count +=1

"""Print Explanations"""    
def interpretation(z_score):

    interpretation_str = ""

    if z_score <= -7:
        interpretation_str = "Insanely Lower"
    elif z_score <= -5:
        interpretation_str = "Extremely Lower"
    if z_score <= -3:
        interpretation_str = "Signficantly Lower"
    elif z_score  <= -2:
        interpretation_str = " Notably Lower"
    elif z_score  <= -1:
        interpretation_str = "Marginally Lower"
    elif z_score  <= 0:
        interpretation_str = "No significant difference"
    elif z_score  <= 1:
        interpretation_str = "No significant difference"
    elif z_score  <= 2:
        interpretation_str = "Marginally Higher"
    elif z_score  <= 3:
        interpretation_str = "Notably Higher"
    elif z_score  <= 5:
        interpretation_str = "Signficantly Higher"
    elif z_score  <= 7:
        interpretation_str = "Extremely Higher"
    else:
        interpretation_str = "Insanely Higher"

    return(interpretation_str)
    
for index, COI in clusters_df.iterrows():
    print(f"COI {index}:")
    for i, (attribute, attribute_dict) in enumerate(COI['explanation'].items()):
        print(f"{i}) {attribute}: {interpretation(attribute_dict['z_score'])}")
    print()

# #TODO: Think about how to modify clustering to avoid conflicting columns from being clustered
# #TODO: Investigate and Drop explanation attributes where z-score is too low
# #TODO: Change clustering alg to not look at std var in distance but rather have 5% as variation
# #TODO: Investigate why silhouette scores are low and why elbow graph only decreases

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
