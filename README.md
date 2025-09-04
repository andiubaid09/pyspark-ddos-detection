# PySpark RandomForest DDoS Detection
## Deskripsi

Proyek ini merupakan implementasi **RandomForest menggunakan PySpark** untuk mendeteksi serangan **DDoS (Distributed Denial of Service)** pada jaringan.  
Lingkungan proyek dijalankan di **virtual Linux dengan 2 worker**, memanfaatkan kemampuan paralel PySpark untuk memproses dataset besar dengan efisien.
Datasheet yang digunakan adalah datasheet publik yang didapatkan di kaggle.

> ⚠️ Catatan: Model yang dilatih dalam notebook ini **tidak disimpan** sebagai file terpisah. Notebook berisi pipeline lengkap untuk pelatihan dan evaluasi. Untuk menggunakan model, jalankan ulang notebook dengan dataset yang tersedia.

---

## Fitur
- Menghubungkan Spark ke Hadoop (lokasi penyimpanan datasheet)
- Preprocessing dataset jaringan untuk deteksi DDoS.  
- Training model RandomForest menggunakan PySpark MLlib.  
- Evaluasi akurasi

---
