import pandas as pd

from sklearn.ensemble import IsolationForest

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

model = IsolationForest()

model.fit(X)

joblib.dump(
    model,
    "models/anomaly_model.pkl"
)
