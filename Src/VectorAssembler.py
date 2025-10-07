from pyspark.ml.feature import VectorAssembler

kolom_fitur = ['dt','dur','dur_nsec','tot_dur','pktrate','Protocol_encoding','port_no','tx_kbps','rx_kbps','tot_kbps']
TARGET = 'label'
df_clean = df_clean.withColumn(TARGET, col(TARGET).cast("double"))
                               
assembler = VectorAssembler (inputCols=kolom_fitur,outputCol="features")
df_vector = assembler.transform(df_clean)
df_final = df_vector.withColumnRenamed(TARGET, 'label')
