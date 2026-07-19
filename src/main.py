# src/main.py
import sys
import os
# Menambahkan root folder ke sys.path agar impor lokal src lancar saat di-run via terminal
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import load_raw_data, save_processed_data
from src.utils import preprocess_data, find_elbow, save_plots
from src.model import evaluate_k_ranges, fit_final_kmeans

def run_pipeline():
    print("=========================================")
    # 1. Load Data
    df = load_raw_data()
    
    # 2. Preprocessing & Scaling
    print("\n[Tahap 1] Preprocessing & Feature Scaling...")
    df, X_normalized = preprocess_data(df)
    
    # 3. Cari K Optimal
    print("\n[Tahap 2] Mencari K Optimal...")
    k_range, inertia, silhouette = evaluate_k_ranges(X_normalized)
    best_k = find_elbow(k_range, inertia)
    print(f"🎯 K Optimal terdeteksi secara matematis: K = {best_k}")
    
    # (Opsional) Di sini kamu bisa selipkan kode visualisasi grafik elbow 
    # memanfaatkan fungsi dari utils.py
    
    # 4. Fitting Model Final (Misal dipilih K=3 sesuai keputusan risetmu)
    print(f"\n[Tahap 3] Fitting Model Final K=3...")
    df_final, model = fit_final_kmeans(df, X_normalized, n_clusters=3)
    
    # 5. Ekspor Hasil Akhir
    print("\n[Tahap 4] Menyimpan Hasil...")
    save_processed_data(df_final)
    print("=========================================")
    print("Pipeline Selesai Dijalankan!")

if __name__ == '__main__':
    run_pipeline()