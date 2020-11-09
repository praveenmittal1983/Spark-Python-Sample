CREATE TEMPORARY VIEW RAW_DATA
USING org.apache.spark.sql.parquet
OPTIONS (
  path "/MyApp/spark-warehouse/myapp.db/raw_data"
);

CREATE TEMPORARY VIEW RAW_DATA_ADDITIONAL_COLUMNS
USING org.apache.spark.sql.parquet
OPTIONS (
  path "/MyApp/spark-warehouse/myapp.db/raw_data_additional_columns"
);

CREATE TEMPORARY VIEW CHARACTERS_BY_COMIC
USING org.apache.spark.sql.parquet
OPTIONS (
  path "/MyApp/spark-warehouse/myapp.db/characters_by_comic"
);