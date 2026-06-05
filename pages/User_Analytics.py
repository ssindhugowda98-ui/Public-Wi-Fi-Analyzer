import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

sessions,nodes = load_data()

st.title("👤 User Analytics")

fig = px.histogram(
    sessions,
    x="connection_duration_secs",
    nbins=30,
    title="Session Duration Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig2 = px.histogram(
    sessions,
    x="data_mb",
    nbins=30,
    title="Data Consumption Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
