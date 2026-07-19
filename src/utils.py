# src/utils.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """Tahap pembersihan, filter, log transform, dan standardisasi"""
    # 1. Drop NA dan filter ulasan > 100
    df = df.dropna(subset=['totalScore', 'reviewsCount'])
    df = df[df['reviewsCount'] > 100].copy()
    
    # 2. Log Transform
    df['reviewsCount_log'] = np.log1p(df['reviewsCount'])
    
    # 3. Feature Scaling
    X = df[['totalScore', 'reviewsCount_log']]
    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)
    
    return df, X_normalized

def find_elbow(k_values, inertia_values):
    """Fungsi matematis mencari siku (elbow) terbaik"""
    k_values = list(k_values)
    x1, y1 = k_values[0], inertia_values[0]
    x2, y2 = k_values[-1], inertia_values[-1]
    distances = []
    for i in range(len(k_values)):
        x0, y0 = k_values[i], inertia_values[i]
        num = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
        den = np.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        distances.append(num / den)
    return k_values[np.argmax(distances)]

def save_plots(fig, filename):
    """Helper untuk menyimpan plot grafik ke folder root atau reports"""
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✅ Grafik tersimpan sebagai '{filename}'")
    plt.close(fig) # Menutup plot agar hemat memori saat dijalankan via terminal