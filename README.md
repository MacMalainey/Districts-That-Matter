# Districts-That-Matter

## Requirements

The project will only work on a Linux system that satisfies the following:
- Python 3.10+
- Pip for Python 3.10+ (version must match version of Python)
- Node 18+
- SQLite3
- Spatialite

### Installing requirements

To install the requirements on an Ubuntu system run:
```bash
sudo apt install python3 python3-pip python3-venv libsqlite3-mod-spatialite spatialite-bin
sudo snap install node --classic
```

### Downloading Data

This project relies on census data downloaded from Stats Canada. **THE DATA FILES ARE LARGE AND TAKE ABOUT 15 MINUTES TO DOWNLOAD!**

#### Census Data [Link](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger.cfm?Lang=E&SearchText=toronto&DGUIDlist=2021A00053520005&GENDERlist=1&STATISTIClist=1&HEADERlist=0)

1. Click the link above
2. Open `Comprehensive Download Files`
3. Download `Canada, provinces, territories, census divisions (CDs), census subdivisions (CSDs) and dissemination areas (DAs) - Ontario only` in the `csv` format
4. Extract **ALL** files into the project's `.local` folder
5. Verify the following files exist:
    - `.local/98-401-X2021006_English_CSV_data_Ontario.csv`
    - `.local/98-401-X2021006_Geo_starting_row_Ontario.CSV`

#### Boundary Data [Link](https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?year=21)

1. Click the link above
2. Under `Type` select `Digital Boundary Files (DBF)`
3. Under `Statistical Boundaries` select `Dissemination Areas`
4. Under `Format` select `Shapefile (.shp)`
5. Click `Continue`
6. Download the document `lda_000a21a_e.zip`
7. Extract **ALL** files into the project's `.local` folder
8. Verify the following files exist:
    - `.local/lda_000a21a_e.cph`
    - `.local/lda_000a21a_e.dbf`
    - `.local/lda_000a21a_e.prj`
    - `.local/lda_000a21a_e.sbn`
    - `.local/lda_000a21a_e.sbx`
    - `.local/lda_000a21a_e.shp`
    - `.local/lda_000a21a_e.shx`

## Running the Project

Once the requirements are satisfied and the data has been downloaded and extracted into the proper location - you can run the project.

### Initialization steps (only run once)

```bash
# Download all packages required to build the code (doesn't download what is described above)
./setup.sh
# Initialize the database and load the data into it
# NOTE: This step takes about 15 minutes
./initdb.sh
```
