import pandas as pd

from sklearn.ensemble import RandomForestRegressor

import joblib

df = pd.read_csv(
    "data/wifi_sessions.csv"
)

df["timestamp"] = pd.to_datetime(
    df["timestamp"]
)

df["hour"] = df["timestamp"].dt.hour

df["day"] = df["timestamp"].dt.day

df["month"] = df["timestamp"].dt.month

traffic = (
    df.groupby(
        ["node_id","hour","day","month"]
    )
    .size()
    .reset_index(name="sessions")
)

traffic["node_id"] = (
    traffic["node_id"]
    .astype("category")
    .cat.codes
)

X = traffic[
    ["node_id","hour","day","month"]
]

y = traffic["sessions"]

model = RandomForestRegressor()

model.fit(X,y)

joblib.dump(
    model,
    "models/traffic_predictor.pkl"
)

print("saved")
