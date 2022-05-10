from pyspark.sql.functions import upper
from pyspark.sql.functions import col

def load_config_file(spark,config_file_location,table_name) :
    config_df_with_spaces = spark.read.format("csv").option("header", "true").option("inferSchema", "false").load(
        config_file_location)
    config_df = config_df_with_spaces.filter(upper(col("TABLE_NAME")) == table_name)
    config_df.show()

