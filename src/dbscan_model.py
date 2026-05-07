from sklearn.cluster import DBSCAN

def run_dbscan(X_scaled):
    model = DBSCAN(
        eps=2.5,
        min_samples=10,
        algorithm="brute"
    )

    labels = model.fit_predict(X_scaled)
    return labels