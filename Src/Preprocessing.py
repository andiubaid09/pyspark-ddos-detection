from pyspark.sql.functions import col, sum, count, lit
from pyspark.sql.functions import col, sum, when
from pyspark.ml.feature import StringIndexer

df.select([sum(col(c).isNull().cast("int")).alias(c) for c in df.columns]).show()
missing_df = df.select([sum(col(c).isNull().cast("int")).alias(c) for c in df.columns])

total_rows = df.count()
print(f"Jumlah rows adalah : {total_rows}")
missing_counts = [count(when(col(c).isNull(),c)).alias(f'Jumlah_NULL_{c}')for c in df.columns]
missing_df = df.agg(*missing_counts)
if total_rows == 0:
    print("DataFrame kosong.")
else:
    print("Ringkasan Missing Values (NULL) per kolom:")

missing_row = missing_df.collect()[0]
print("{:<30} {:<15} {:<15}".format("Kolom", "Jumlah NULL", "Persentase (%)"))
print("="*60)
for c in df.columns:
    count_null = missing_row[f'Jumlah_NULL_{c}']
    percent_null = round((count_null / total_rows) * 100, 2)
    print("{:<30} {:<15}{:<15}".format(c, count_null, f"{percent_null}%"))


# Menghapus kolom missing values

kolom_missing = ["rx_kbps","tot_kbps"]
df_clean = df.na.drop(subset=kolom_missing)
print(f"Jumlah baris awal: {df.count()}")
print(f"Jumlah baris setelah di cleaning: {df_clean.count()}")

# Menangani kolom kategorial

Protocol_encoding = StringIndexer(inputCol="Protocol",outputCol="Protocol_encoding")
df_clean = Protocol_encoding.fit(df_clean).transform(df_clean)

print("\Pemetaan dari StringIndexer:")
df_clean.select("Protocol","Protocol_encoding").distinct().orderBy("Protocol_encoding").show()