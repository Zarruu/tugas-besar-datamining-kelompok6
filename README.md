# tugas-besar-datamining-kelompok6
## 🚀 Cara Menjalankan

### ✅ 1. Persiapkan Environment

Install dependensi:
```bash
pip install -r requirements.txt
```

### ✅ 2. Jalankan Pipeline

#### 💻 Via Terminal:
```bash
bash run.sh
```

#### 📒 Via Jupyter Notebook:
Buka dan jalankan:
```text
src/main_notebook.ipynb
```

---

## 📦 Struktur Modular

- **`data_loader.py`**: fungsi `load_raw_data()` dan `save_processed_data()`
- **`model.py`**: fungsi `train_model()`, split data, dan prediksi
- **`utils.py`**: evaluasi model (akurasi, classification report, dll.)

---

## 📓 Catatan

- Semua path diasumsikan relatif dari root project
- Tambahkan file data kamu ke dalam `data/raw/`
- Hasil preprocessing disimpan di `data/processed/` 
- Pastikan target label diberi nama kolom `target` (atau sesuaikan di script)

---

## 👩‍💻 Kontributor

- Hadi Muhammad Yusuf
- Muhammad Nizar Akmal
- Ananda Raka Aditya Wilangga
- Muflih Afif Mukhtalif

---

## 📄 Lisensi

Proyek ini bersifat open-source dan bebas digunakan untuk edukasi dan pengembangan pribadi.