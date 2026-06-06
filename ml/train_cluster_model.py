import pandas as pd

from sklearn.cluster import KMeans

import joblib

df = pd.read_csv(
    "data/wifi_sessions.csv"
)

df["data_mb"] = (
    df["bytes_transferred"]
    /1024
    /1024
)

X = df[
    [
        "data_mb",
        "connection_duration_secs"
    ]
]

model = KMeans(
    n_clusters=3,
    random_state=42
)

model.fit(X)

joblib.dump(
    model,
    "models/cluster_model.pkl"
)
