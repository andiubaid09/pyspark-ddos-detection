train_data, test_data = df_final.randomSplit([0.8, 0.2],seed=42)

print(f"Jumlah data train: {train_data.count()}")
print(f"Jumlah data test: {test_data.count()}")