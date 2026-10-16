import streamlit as st
import pandas as pd

st.title("Player Performance Dashboard")

df = pd.DataFrame({
    "Player": ["Rohit", "Virat", "Rahul", "Sky", "Hardik"],
    "Runs": [65, 88, 45, 72, 40]
})

player = st.selectbox("Select Player", df["Player"])

st.write("Runs scored:", df[df["Player"] == player]["Runs"].values[0])
st.bar_chart(df[df["Player"] == player], x="Player", y="Runs")
