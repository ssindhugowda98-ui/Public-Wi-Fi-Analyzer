import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

sessions,nodes = load_data()

st.title("⏰ Time Analysis")

hourly = (
    sessions.groupby("hour")
    .size()
    .reset_index(name="sessions")
)

fig = px.line(
    hourly,
    x="hour",
    y="sessions",
    markers=True,
    title="Hourly Usage Pattern"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

daily = (
    sessions.groupby("date")
    .size()
    .reset_index(name="sessions")
)

fig2 = px.area(
    daily,
    x="date",
    y="sessions",
    title="Daily Traffic Trend"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
