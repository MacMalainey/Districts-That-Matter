import os
import numpy
import shapely
import spatialite
from libpysal.weights import Queen
import pandas as pd
import geopandas as gpd
import queries
import matplotlib.pyplot as plt
import json
from sklearn.cluster import AgglomerativeClustering


""" Get data from database and create pandas frame"""
db = spatialite.connect(
            os.path.dirname(__file__) + "/../.local/dtmTORO.db"
        )

query = "SELECT *, AsText(bd.geometry) AS geometry_wkt FROM census_data AS cd, boundary_data AS bd USING (dguid);"

pd_df = pd.read_sql(query,db)


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
    pd_df[col_name] = pd_df[col_name] / pd_df["rc_visible_minority"]  * 100

# The column names below is the only one where inf values are possible if rc (for visible minoirties) = 0 yet there are still
# those who are not visible minorities
pd_df['visible_minority_not_applicable'] = pd_df['visible_minority_not_applicable'].replace([float('inf'), float('-inf')], 100)


""" Create geopandas dataframe and contiguiuty weights matrix """

pd_df['geometry'] = pd_df['geometry_wkt'].apply(lambda x: shapely.from_wkt(x))

gpd_df = gpd.GeoDataFrame(pd_df, crs="EPSG:4326", geometry="geometry")

contiguity_weights = Queen.from_dataframe(gpd_df, use_index=True)


""" Clustering """
# Set seed for reproducibility
numpy.random.seed(0)
# Initialize the algorithm
model = AgglomerativeClustering(linkage="ward", n_clusters=5)
# Fill in null values
df_cluster_cols = gpd_df[schema["ages"] + schema["marital_status"] + schema["household"] + schema["income"] + schema["immigrated"] + schema["birthplace"] + schema["generation"] + schema["visible_minority"]]
df_filled = df_cluster_cols.fillna(df_cluster_cols.mean())
# Run clustering ( WITHOUT REGIONALIZATION RIGHT NOW)
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


"""Code Snippets for Debugging"""

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
