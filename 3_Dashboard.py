import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.title("📊 Dashboard")

conn = sqlite3.connect("nac_system.db")
df = pd.read_sql("SELECT * FROM loadsheet", conn)
conn.close()

st.dataframe(df)

if not df.empty:
    fig, ax = plt.subplots()
    ax.plot(df["zfw"])
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.plot(df["pax"])
    st.pyplot(fig2)
