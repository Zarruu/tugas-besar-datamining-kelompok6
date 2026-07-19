# src/data_loader.py
import pandas as pd
import os

def load_raw_data(file_path='data/raw/raw_dataset_pulau_jawa.csv'):
    """Memuat dataset pariwisata mentah"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset tidak ditemukan di {file_path}")
    print(f"Memuat dataset: {file_path}")
    df = pd.read_csv(file_path)
    return df

def save_processed_data(df, output_path='data/processed/hasil_clustering_pulau_jawa_lengkap.csv'):
    """Menyimpan hasil akhir clustering ke folder processed"""
    # Pastikan folder processed ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Bersihkan kolom duplikat/temporary sebelum ekspor sesuai kodemu
    cols_to_keep = [col for col in df.columns if col not in ['Cluster_K3', 'Cluster_K4', 'Cluster_Name_K3', 'Cluster_Name_K4']]
    df_export = df[cols_to_keep]
    
    df_export.to_csv(output_path, index=False)
    print(f"✅ Hasil lengkap tersimpan di: {output_path}")