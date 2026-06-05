import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

sessions,nodes = load_data()

st.title("🔥 Hotspot Analytics")

hotspots = (
    sessions.groupby("node_id")
    .size()
    .reset_index(name="sessions")
)

hotspots = hotspots.sort_values(
    "sessions",
    ascending=False
)

fig = px.bar(
    hotspots.head(10),
    x="node_id",
    y="sessions",
    title="Top 10 Busiest Hotspots"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
