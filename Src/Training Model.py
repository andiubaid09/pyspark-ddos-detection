from pyspark.ml.classification import RandomForestClassifier

rf = RandomForestClassifier(labelCol='label',featuresCol='features', numTrees=100, seed=42)
model = rf.fit(train_data)