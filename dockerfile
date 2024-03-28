# syntax=docker/dockerfile:1
FROM python:3 AS dtm_base
RUN apt update
RUN apt install -y sqlite3 libsqlite3-mod-spatialite
ENV PYTHONUNBUFFERED=1

FROM dtm_base AS build_database
RUN apt install -y spatialite-bin
COPY parser/requirements.txt app/requirements.txt
RUN python3 -m pip install -r app/requirements.txt
COPY .local .local
COPY parser app
RUN spatialite -bail -batch "dtmTORO.db" ""
RUN python3 app/main.py ".local/98-401-X2021006_English_CSV_data_Ontario.csv" --schema "app/characteristics.csv" --filter "app/GTA_CSD_LIST.txt" --output "dtmTORO.db"
RUN echo "Loading boundary data..."
RUN spatialite -bail -batch "dtmTORO.db" < "app/load_boundary.sql"
RUN rm -rf .local app

FROM node:21-alpine3.18 AS build_webapp
WORKDIR /app
COPY districts_tm/package.json package.json
COPY districts_tm/package-lock.json package-lock.json
RUN npm install
COPY districts_tm/src src
COPY districts_tm/public public
RUN npm run build

FROM dtm_base AS final
WORKDIR /app
COPY server/requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY --from=build_database dtmTORO* /app/
COPY --from=build_webapp /app/build /app/static
COPY server /app
ENV DTM_SERVER_STATIC_DIR=/app/static
ENV DTM_SERVER_SCHEMA=/app/dtmTORO_schema.json
ENV DTM_SERVER_DATABASE=/app/dtmTORO.db
CMD ["python3", "-m", "flask", "--app", "main", "run", "--host", "0.0.0.0"]








