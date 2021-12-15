# Spark-Python-Sample

## Objective:

MyApp does following:

1. Reads 'marvel_dc_characters.csv' file using [pySpark - DataFrames]
2. Groups Character details by Comic.
3. Loads the grouped data as parquet file and json file.
4. To query parquet files, use [tools/spark-sql.sh]. This creates required Temporary Views.

## Structure:

MyApp has following structure

1. [MyApp.py] is main module of this App. This is the entry point of program.
2. [tools, sql] folder contains scripts to run Spark SQL database and Jupyter Notebook.
3. [analysis] folder contain Jupyter notebook to analyse and understand the data.
4. [data, output, common, log] folder is used to include supporting framework like source & target data, logging.

## Running App

Following are the steps to start 'MyApp'

1. Download Repository
2. Run [Dockerfile] using command `docker build -t myapp .`. Note, this might take ~20 minutes and ~3 Gb of space as it does heavy lifting of all required softwares. I haven't used 3rd party pre-built docker images and I haven't spend time in installing [only] required components within a SDK.
3. Run [DockerImage] using command `docker run -it --rm --name=myapp -p 4040:4040 -p 8888:8888 myapp`
4. Once container shell [bash] is active, run application using command `python MyApp.py`

## Running SparkSQL DB

1. Run script [/MyApp/tools/spark-sql.sh]
2. In SparkSQL console, run 'Show tables'
2. Then, run 'Select * from characters_by_comic Limit 10'

## Running Jupyter Lab

1. Run script [/MyApp/tools/data_analysis.sh]
2. From local machine browser, access URL [http://localhost:8888]

## Running Spark UI

1. While container is running, Spark UI can be accessed from local machine browser using URL [http://localhost:4040]
