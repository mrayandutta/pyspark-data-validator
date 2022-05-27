import findspark

findspark.init()
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("test").getOrCreate()

columns = ["id","salary","department"]
data = [(1,1000,"IT"), (2,1500,"HR"), (3,500,"Marketing")]
rdd = spark.sparkContext.parallelize(data)
df = rdd.toDF(columns)
df.show()
win_spec_by_department = Window.partitionBy('department')
avg_salary_df = df.withColumn("average salary",avg("salary").over(win_spec_by_department))
avg_salary_df.show()