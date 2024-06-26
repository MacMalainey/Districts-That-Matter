# Districts-That-Matter

## Requirements

This project requires access to a Linux system that has Docker and a web browser installed

### Installing Docker

If you don't already have Docker installed (check by running `docker -v` in your terminal) you can install the desktop client [here](https://www.docker.com/products/docker-desktop/) and then verify it's installation using `docker -v`.

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

```bash
# DO NOT RUN 'parser/run.sh' or 'server/run.sh'
# On first execution this will build the application - this will take a while
./run.sh
```

Once the script finishes open your web browser to [127.0.0.1:5000](http://127.0.0.1:5000)
