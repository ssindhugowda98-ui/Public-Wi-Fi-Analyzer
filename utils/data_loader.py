import pandas as pd

def load_data():

    sessions = pd.read_csv(
        "data/wifi_sessions.csv"
    )

    nodes = pd.read_csv(
        "data/wifi_nodes.csv"
    )

    sessions["timestamp"] = pd.to_datetime(
        sessions["timestamp"]
    )

    sessions["hour"] = sessions["timestamp"].dt.hour

    sessions["date"] = sessions["timestamp"].dt.date

    sessions["data_mb"] = (
        sessions["bytes_transferred"]
        / 1024
        / 1024
    )

    return sessions, nodes
