import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

sessions,nodes = load_data()

sessions["lat"] = sessions[
    "coordinates"
].str.extract(
    r"\[(.*?),"
).astype(float)

sessions["lon"] = sessions[
    "coordinates"
].str.extract(
    r",(.*?)\]"
).astype(float)

st.title("🗺️ Geospatial Analysis")

fig = px.scatter_map(
    sessions,
    lat="lat",
    lon="lon",
    zoom=10,
    title="Hotspot Locations"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
