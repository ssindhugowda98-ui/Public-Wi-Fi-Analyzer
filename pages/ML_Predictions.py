import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.title(
    "🤖 Machine Learning Predictions"
)

df = pd.read_csv(
    "data/wifi_sessions.csv"
)

df["data_mb"] = (
    df["bytes_transferred"]
    /1024
    /1024
)

# -----------------
# USER CLUSTERING
# -----------------

cluster_model = joblib.load(
    "models/cluster_model.pkl"
)

df["cluster"] = (
    cluster_model.predict(
        df[
            [
             "data_mb",
             "connection_duration_secs"
            ]
        ]
    )
)

fig = px.scatter(
    df,
    x="data_mb",
    y="connection_duration_secs",
    color="cluster",
    title="User Segmentation"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------
# ANOMALY
# -----------------

anomaly_model = joblib.load(
    "models/anomaly_model.pkl"
)

df["anomaly"] = (
    anomaly_model.predict(
        df[
            [
             "data_mb",
             "connection_duration_secs"
            ]
        ]
    )
)

anomaly_df = df[
    df["anomaly"] == -1
]

st.subheader(
    "⚠ Suspicious Sessions"
)

st.dataframe(
    anomaly_df.head(20)
)
