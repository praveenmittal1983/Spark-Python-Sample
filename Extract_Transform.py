from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import *

class pySparkSession():

    jsonSchema = StructType([
        StructField("EmployeeID", IntegerType(),True),
        StructField("EmployeeName", StringType(),True),
        StructField("DepartmentID", IntegerType(),True),
        StructField("EmployeeAge", IntegerType(),False)
        ])

    def __init__(self, AppName):
        # Create a SparkSession
        self.spark = SparkSession \
            .builder \
            .appName(AppName) \
            .config("spark.some.config.option", "some-value") \
            .getOrCreate()

    def create_TempView(self, filename, type, headers, multiLine, view_name):
        #Create Temporary View
        create_df = self.spark.read.format(type) \
                        .option('header', bool(headers)) \
                        .option('multiLine', bool(multiLine)) \
                        .load(filename)

        create_df.createOrReplaceTempView(view_name)

    # #Create Department Temporary View
    # create_df = spark.read.format('csv') \
    #                 .option('header',True) \
    #                 .option('multiLine', True) \
    #                 .load('data//2.csv')

    # create_df.createOrReplaceTempView('Dept')

    # spark.sql('SELECT EID, EName, DID, Age FROM Emp').show()
    # spark.sql('SELECT * FROM Dept').show()
    # spark.sql('SELECT * FROM Emp E LEFT OUTER JOIN Dept D on E.DID == D.DID').show()

    def getdata_TempView(self, view_name):
        return self.spark.sql('''
            SELECT 
            cast(EID as int) as Employee_ID,
            EName as Employee_Name,
            cast(DID as int) as Department_ID,
            cast(age as int) as Age
            FROM 
            ''' + view_name)

    def load_data(self, data_frame):
        print (data_frame.schema)
        # data_frame.write.mode(overwrite).json('data//1.json')
        # .format('json').save('data')
        # data_frame.write.mode('overwrite').json('output')
        data_frame.write.mode('append').saveAsTable('T1')

    def mapper(self, line):
        print (line)
        fields = line.split(',')
        print (fields)
        return Row(EID=int(fields[0]), EName=str(fields[1].encode("utf-8")), DID=int(fields[2]), Age=int(fields[3]))

if __name__ == "__main__":
    sc = pySparkSession('MyApp')
    sc.create_TempView('data//1.csv','csv',True,False,'Emp')
    sc.create_TempView('data//2.csv','csv',True,False,'Dept')
    
    sc.load_data(sc.getdata_TempView('Emp'))
    # sc.getdata_TempView('Dept')
    print ('Hello')