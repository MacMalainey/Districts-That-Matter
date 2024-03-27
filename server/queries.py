import spatialite
import pandas as pd

def query_munits(db: spatialite.Connection) -> pd.DataFrame:
    '''
    Queries map unit demographcs from database

    Fulfills FR4, FR12
    '''

    return pd.read_sql(
        "SELECT cd.*, AsText(bd.geometry) AS geometry_wkt FROM census_data AS cd, boundary_data AS bd USING (dguid);",
        db,
        "dguid"
    )

def query_districts_dataframe(db: spatialite.Connection) -> pd.DataFrame:
    """
    Queries all defined districts from the database

    Fulfills FR21
    """

    return pd.read_sql(
        "SELECT dguid, id as district FROM districts WHERE id IS NOT NULL",
        db,
        "dguid",
    )

def insert_districts(db: spatialite.Connection, districts: list[tuple[str, int | None]]):
    cur = db.cursor()
    cur.executemany("INSERT OR REPLACE INTO districts(dguid, id) VALUES (?, ?)", districts)
    db.commit()
