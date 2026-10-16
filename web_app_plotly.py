import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Cricket Multi-Metric Dashboard")

df = pd.DataFrame({
    "Match": [1,2,3,4,5,6],
    "Runs": [45,78,102,56,89,120],
    "StrikeRate": [110,125,140,115,130,150]
})

fig1 = px.line(df, x="Match", y="Runs", title="Runs per Match")
fig2 = px.line(df, x="Match", y="StrikeRate", title="Strike Rate per Match")

st.plotly_chart(fig1)
st.plotly_chart(fig2)
