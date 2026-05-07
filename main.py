from src.preprocess import load_data, clean_data, prepare_features
from src.dbscan_model import run_dbscan
from src.visualize import plot_pca
from sklearn.decomposition import PCA

DATA_PATH = "data/ddos_friday.parquet"

df = load_data(DATA_PATH)
df = clean_data(df)

# smaller sample for DBSCAN
df = df.sample(n=3000, random_state=42)

X_scaled, y_true, feature_names = prepare_features(df)

# reduce dimensions before DBSCAN
pca = PCA(n_components=2, random_state=42)
X_reduced = pca.fit_transform(X_scaled)

dbscan_labels = run_dbscan(X_reduced)

df["dbscan_label"] = dbscan_labels
df["dbscan_prediction"] = df["dbscan_label"].apply(
    lambda x: "Anomaly" if x == -1 else "Normal"
)

df.to_csv("results/anomaly_results.csv", index=False)

plot_pca(
    X_scaled,
    dbscan_labels,
    "results/plots/dbscan_pca.png"
)

print("Project completed.")
print("Total rows:", len(df))
print("Detected anomalies:", (dbscan_labels == -1).sum())