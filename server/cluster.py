import os
import shapely
import spatialite
from libpysal.weights import Queen
import pandas as pd
import geopandas as gpd
import queries
import matplotlib.pyplot as plt

#plt.switch_backend("TkAgg")

db = spatialite.connect(
            os.path.dirname(__file__) + "/../.local/dtmTORO.db"
        )

query = "SELECT *, AsText(bd.geometry) AS geometry_wkt FROM census_data AS cd, boundary_data AS bd USING (dguid);"

pd_df = pd.read_sql(query,db)

pd_df['geometry'] = pd_df['geometry_wkt'].apply(lambda x: shapely.from_wkt(x))

print(pd_df.head())

gpd_df = gpd.GeoDataFrame(pd_df, crs="EPSG:4326", geometry="geometry")

print(gpd_df.head())

gpd_df.plot(
        column="ages_0_to_4",
        scheme="natural_breaks",
        linewidth=0,
        cmap="RdPu",
        legend=True,
)

plt.savefig('plot.png')

# with spatialite.Connection(os.path.dirname(__file__) + "/../.local/dtmTORO.db") as db:
#     data = queries.query_munit_demographics_polygons(db)
#     print(data)
#     panda_df = geopandas.GeoDataFrame(data, geometry="geometry")