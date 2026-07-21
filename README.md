# tugas-besar-datamining-kelompok6
# Rancang Bangun Sistem Rekomendasi Wisata Pulau Jawa

## Anggota Kelompok & NIM (Kelompok 6)
- **Hadi Muhammad Yusuf** (714230019)
- **Muflih Afif Mukhtalif** (714230012)
- **Muhammad Nizar Akmal** (714230007)
- **Ananda Raka Wilangga** (714230023)

## Deskripsi Kasus
Pulau Jawa merupakan wilayah dengan potensi pariwisata yang sangat besar. Namun, pertumbuhan pesat dan melimpahnya pilihan destinasi sering memicu masalah kelebihan informasi (*information overload*) bagi wisatawan saat merencanakan perjalanan. 

Proyek ini bertujuan untuk membangun sebuah basis pengetahuan (*knowledge base*) bagi sistem rekomendasi destinasi wisata di Pulau Jawa. Dengan mengadopsi kerangka kerja CRISP-DM, proyek ini memanfaatkan teknik *Data Mining* untuk memproses ribuan data *User-Generated Content* (UGC) berupa *rating* dan jumlah ulasan. Hasil akhirnya adalah segmentasi objek wisata secara otomatis menjadi beberapa klaster bermakna yang dapat digunakan untuk merekomendasikan rute perjalanan yang lebih personal dan objektif.

## Sumber Dataset
Dataset dalam penelitian ini merupakan data sekunder (Point of Interest/POI) yang diekstraksi dari **Google Maps**. Proses pengumpulan data dilakukan menggunakan teknik *web scraping* melalui platform otomasi *cloud* **Apify** pada periode 2 hingga 16 Juni 2026. Data mentah berisikan 1090 baris destinasi wisata yang tersebar di wilayah utama Pulau Jawa.

## Langkah Preprocessing
Untuk memastikan kualitas data sebelum dimasukkan ke dalam algoritma, dilakukan tahapan prapemrosesan berikut:
1. **Data Cleaning:** Menghapus baris dengan nilai kosong (*Null/Missing Values*) pada kolom target dan mengeleminasi destinasi wisata yang berada di luar Pulau Jawa.
2. **Text Cleaning:** Memperbaiki penulisan nama kota yang masih berupa singkatan menjadi nama lengkap agar seragam.
3. **Regex Replacement:** Menerjemahkan format penamaan kota dari bahasa inggris ke bahasa Indonesia.
4. **Domain Filtering:** Menghapus baris data yang wilayahnya tidak termasuk dalam Pulau Jawa.
5. **Feature Selection:** Membuang kolom yang tidak perlu, hanya mempertahankan 5 kolom esensial untuk dianalisis.
6. **Filtering:** Menyaring destinasi wisata untuk hanya mempertahankan lokasi dengan jumlah ulasan minimal 100 (`reviewsCount > 100`) guna menjaga validitas popularitas.
7. **Log Transformation:** Menerapkan transformasi matematis logaritmik (`np.log1p`) pada kolom `reviewsCount` untuk mengatasi ketimpangan distribusi data yang sangat ekstrem (*right-skewed*).
8. **Feature Scaling:** Melakukan standardisasi fitur menggunakan `StandardScaler` agar rentang nilai *rating* (1-5) dan jumlah ulasan (puluhan ribu) memiliki bobot yang setara saat dihitung jaraknya oleh algoritma.

## Algoritma yang Digunakan
- **K-Means Clustering:** Algoritma *unsupervised learning* yang digunakan untuk mensegmentasi destinasi wisata ke dalam beberapa kelompok homogen berdasarkan jarak *Euclidean*.

## Evaluasi & Hasil
Pemodelan dievaluasi menggunakan dua metrik internal, yaitu **Elbow Method (Inertia)** dan **Silhouette Coefficient**.
1. **Elbow Method (Inertia / WCSS):**
Mengukur total jarak kuadrat antara setiap titik data dengan pusat klasternya (*centroid*). Semakin kecil nilai Inertia, semakin rapat data di dalam satu klaster. Penurunan nilai Inertia dari $K=2$ ke $K=3$ terbukti sangat signifikan. Setelah $K=3$, penurunan nilai Inertia mulai melambat (*plateau*), menandakan bahwa menambah klaster baru setelah $K=3$ tidak lagi memberikan peningkatan kerapatan yang signifikan.

2. **Silhouette Coefficient:**
Mengukur seberapa mirip suatu data dengan klasternya sendiri dibandingkan dengan klaster terdekat lainnya (*range* nilai $-1$ hingga $+1$). Semakin mendekati $1$, semakin jelas pemisahan/separasi antar-klaster. Skenario **$K=3$ menghasilkan Silhouette Score tertinggi (`0.3668`)**, mengonfirmasi bahwa $K=3$ memiliki struktur pemisahan yang paling optimal dibanding rentang $K$ lainnya ($K=2$ hingga $K=10$).
- **Hasil Pengujian:** Eksperimen iteratif dilakukan dari K=2 hingga K=10. Skenario terbaik ditemukan pada **K=3**.
- **Metrik Model (K=3):** 
  - Silhouette Score: `0.3668` (Terbaik, menunjukkan separasi antar klaster yang tegas).
  - Inertia (WCSS): `795.070`.
- **Interpretasi Klaster:**
  1. **Cluster Khusus / Niche (Hijau):** Destinasi *hidden gem* atau baru dengan jumlah ulasan paling rendah dan rating bervariasi.
  2. **Cluster Populer Sedang (Oranye):** Destinasi wisata lokal dengan jumlah ulasan menengah dan rating stabil.
  3. **Cluster Populer Tinggi (Biru):** *Landmark* utama dengan jumlah ulasan sangat masif dan rating konsisten tinggi.

## Cara Menjalankan (Run Notebook/Script)
1. **Clone Repository:**
   ```bash
   git clone [https://github.com/namauser/tugas-besar-datamining-kelompok6.git](https://github.com/namauser/tugas-besar-datamining-kelompok6.git)
   cd tugas-besar-datamining-kelompok6

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
