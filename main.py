import streamlit as st
from database import init_db

init_db()

st.set_page_config(
    page_title="NAC OCC Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------- CUSTOM STYLE --------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.metric-card {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.title("✈️ NAC OPERATIONS CONTROL CENTER (OCC)")

st.markdown("### Real-Time Flight Operations System")

st.markdown("---")

st.info("System Ready ✅ | Designed by Guru Shah")
