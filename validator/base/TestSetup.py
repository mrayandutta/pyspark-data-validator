from pyspark.sql import SparkSession

spark_session = SparkSession.builder.appName("test").getOrCreate()
spark_session.createDataFrame([(1, "value1"), (2, "value2")], ["id", "value"]).show()