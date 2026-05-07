import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plot_pca(X_scaled, labels, save_path):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    plt.figure(figsize=(8, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, s=3)
    plt.title("DBSCAN Network Traffic Anomaly Detection")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.savefig(save_path, dpi=300)
    plt.close()