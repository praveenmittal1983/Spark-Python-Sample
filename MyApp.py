from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions as F
from common import log

class pySparkSession():

    def __init__(self, AppName):

        # Create a SparkSession
        self.spark = SparkSession \
            .builder \
            .appName(AppName) \
            .config("spark.some.config.option", "some-value") \
            .getOrCreate()
        
        #Setup Database
        self.spark.sql('CREATE DATABASE IF NOT EXISTS MyApp')
        self.spark.sql('USE MyApp')


    def loadData(self, filename, type, headers, multiLine):
        #Load Data into DataFrame
        create_df = self.spark.read.format(type) \
                        .option('header', bool(headers)) \
                        .option('multiLine', bool(multiLine)) \
                        .option('encoding','ISO-8859-8') \
                        .load(filename)

        return create_df


    def splitColumn(self, df):
        #OneOff: Split Name into Character and Comic Name
        return df.withColumn('Character', F.trim(F.split(F.col('Name'), '\\(').getItem(0))) \
            .withColumn('Comic_Name', F.regexp_replace(F.split(F.col('Name'), '\\(').getItem(1),'\\)',''))


    def save_TemporaryTables(self, df, tablename):
        #Save as Temporary Tables in Database
        df.write.mode('append').saveAsTable(tablename)


    def save_Json(self, df, path):
        #Save as Json
        df.write.mode('append').json(path)


if __name__ == "__main__":

    ## Setup logging
    logger = log.setLoggerContext()
    logger.info("Starting application {}".format(__name__))

    try:
        logger.info("Initializing application {}".format(__name__))
        sc = pySparkSession('MyApp')
        
        logger.info("Reading RAW data")
        raw_df = sc.loadData('data//marvel_dc_characters.csv//marvel_dc_characters.csv','csv',True,False)
        raw_df_with_additional_cols = sc.splitColumn(raw_df)

        logger.info("Transforming RAW data")
        character_by_comic = raw_df_with_additional_cols.groupBy('Universe','Comic_Name').agg(F.collect_set(
                                                                                                    F.struct("Character", 
                                                                                                    "Gender",
                                                                                                    "Alignment",
                                                                                                    "EyeColor",
                                                                                                    "HairColor",
                                                                                                    "Identity",
                                                                                                    "Status",
                                                                                                    "Appearances",
                                                                                                    "FirstAppearance",
                                                                                                    "Year")
                                                                                                    ).alias("Character_Info"))

        #Save as Parquet Files
        logger.info("Loading as parquet files")
        sc.save_TemporaryTables(raw_df, 'RAW_DATA')
        sc.save_TemporaryTables(raw_df_with_additional_cols, 'RAW_DATA_ADDITIONAL_COLUMNS')
        sc.save_TemporaryTables(character_by_comic, 'CHARACTERS_BY_COMIC')

        #Save as JSON
        logger.info("Loading as json files")
        sc.save_Json(character_by_comic, 'output')
    except Exception as eMsg:
        logger.error('Exception: {}'.format(str(eMsg)))
    finally:
        del sc
        del raw_df, raw_df_with_additional_cols, character_by_comic
        logger.info('Successfully Logout from the application')