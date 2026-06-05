import streamlit as st
from utils.data_loader import load_data
from utils.analytics import get_kpis

sessions,nodes = load_data()

kpi = get_kpis(sessions)

st.title("📊 Overview Dashboard")

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric(
"Sessions",
f"{kpi['sessions']:,}"
)

c2.metric(
"Users",
f"{kpi['users']:,}"
)

c3.metric(
"Data(MB)",
f"{kpi['data']:,.0f}"
)

c4.metric(
"Avg Duration",
f"{kpi['duration']:.1f} min"
)

c5.metric(
"Hotspots",
kpi['hotspots']
)
