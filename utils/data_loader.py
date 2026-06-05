import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():

    filepath = "data/wifi_sessions.csv"

    if not os.path.exists(filepath):
        st.error(f"File not found: {filepath}")
        st.stop()

    if os.path.getsize(filepath) == 0:
        st.error("wifi_sessions.csv is empty")
        st.stop()

    try:
        sessions = pd.read_csv(filepath)
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
        st.stop()

    nodes_path = "data/wifi_nodes.csv"

    if os.path.exists(nodes_path):
        nodes = pd.read_csv(nodes_path)
    else:
        nodes = pd.DataFrame()

    sessions["timestamp"] = pd.to_datetime(
        sessions["timestamp"]
    )

    sessions["hour"] = sessions["timestamp"].dt.hour
    sessions["date"] = sessions["timestamp"].dt.date

    sessions["data_mb"] = (
        sessions["bytes_transferred"]
        /1024
        /1024
    )

    return sessions,nodes
