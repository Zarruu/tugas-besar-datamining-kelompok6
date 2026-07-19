# src/model.py
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd

def evaluate_k_ranges(X_normalized, k_min=2, k_max=10):
    """Menjalankan K-Means untuk deretan K dan menghitung inertia & silhouette"""
    k_range = range(k_min, k_max + 1)
    inertia_list = []
    silhouette_list = []
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_normalized)
        inertia_list.append(kmeans.inertia_)
        sil = silhouette_score(X_normalized, kmeans.labels_)
        silhouette_list.append(sil)
        
    return list(k_range), inertia_list, silhouette_list

def fit_final_kmeans(df, X_normalized, n_clusters=3):
    """Melatih model final dan memetakan nama cluster sesuai kriteria pariwisata"""
    kmeans_model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df['Cluster_Final'] = kmeans_model.fit_predict(X_normalized)
    
    # Logic mapping cluster berdasarkan kebiasaan destinasi pariwisata
    cluster_means = df.groupby('Cluster_Final')['reviewsCount_log'].mean().sort_values()
    
    if n_clusters == 3:
        cluster_labels = ['Cluster Khusus/Niche', 'Populer Sedang', 'Populer Tinggi']
    else:
        cluster_labels = [f'Cluster {i+1}' for i in range(n_clusters)]
        
    cluster_mapping = {cluster_means.index[i]: cluster_labels[i] for i in range(n_clusters)}
    df['Cluster_Name_Final'] = df['Cluster_Final'].map(cluster_mapping)
    
    return df, kmeans_model