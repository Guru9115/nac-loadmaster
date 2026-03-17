import streamlit as st
import re

st.title("📡 LDM Parser")

text = st.text_area("Paste LDM")

if st.button("Parse"):
    pax = re.search(r"PAX/(\d+)", text)
    zfw = re.search(r"ZFW/(\d+)", text)

    st.write("PAX:", pax.group(1) if pax else "N/A")
    st.write("ZFW:", zfw.group(1) if zfw else "N/A")
