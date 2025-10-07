from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .appName("ModelRF_Deteksi_DDoS")
         .master("spark://192.168.56.9:7077")
         .getOrCreate()
        )
csv_path = "hdfs://192.168.56.9:9000/user/hadoop/bigdata/dataset_sdn.csv"

df = (spark.read
      .option("header",True)
      .option("inferSchema",True)
      .csv(csv_path)
     )