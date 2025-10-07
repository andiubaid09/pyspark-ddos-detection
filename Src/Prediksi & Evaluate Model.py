from pyspark.ml.evaluation import MulticlassClassificationEvaluator

prediksi = model.transform(test_data)
print("Hasil prediksi pada data testing (5 baris teratas):")
prediksi.select('label', 'prediction', 'probability').show(5, truncate=False)

# Akurasi
prediksi.select('label','prediction','probability')

evaluator = MulticlassClassificationEvaluator(labelCol='label', predictionCol='prediction', metricName='accuracy')
akurasi = evaluator.evaluate(prediksi)
print(f"Akurasi model:{akurasi}")

#cm
from pyspark.mllib.evaluation import MulticlassMetrics
predictionAndLabels = prediksi.select(['prediction','label']).rdd.map(tuple)

metrics = MulticlassMetrics(predictionAndLabels)
cm = metrics.confusionMatrix().toArray()
print("\nConfusion Matrix:")
print(cm)