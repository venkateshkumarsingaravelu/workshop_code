import streamlit as st
import pandas as pd

st.title("Cricket Runs per Match")

df = pd.DataFrame({
    "Match": [1,2,3,4,5,6],
    "Runs": [45,78,102,56,89,120]
})

st.line_chart(df, x="Match", y="Runs")