import streamlit as st
from datetime import date
from database import insert_loadsheet, init_db
from utils import *

init_db()

st.title("✈️ Loadsheet")

flight = st.text_input("Flight", "RA410")
fdate = st.date_input("Date", date.today())

OA = st.number_input("OA",0,8,2)
OB = st.number_input("OB",0,96,60)
OC = st.number_input("OC",0,54,30)

cargo = st.number_input("Cargo",0,20000,1500)
fuel = st.number_input("Fuel",0,30000,8000)

st.subheader("LMC")
lmc_pax = st.number_input("LMC Pax", -50,50,0)
lmc_cargo = st.number_input("LMC Cargo", -2000,2000,0)

if st.button("Generate"):

    total_pax = OA+OB+OC+lmc_pax
    pax_weight = total_pax * ADULT
    cargo_total = cargo + lmc_cargo

    ZFW = DOW + pax_weight + cargo_total
    TOW = ZFW + fuel
    LW = TOW - fuel*0.8

    index_val = DOI + (total_pax*0.1) + (cargo_total/1000)

    cg = index_to_cg(index_val)
    stab = get_stab_from_cg(cg)

    direction = "UP" if stab>=0 else "DN"

    st.metric("ZFW", int(ZFW))
    st.metric("TOW", int(TOW))
    st.metric("LW", int(LW))

    st.write(f"CG: {cg:.2f}%")
    st.write(f"STAB: {abs(stab)} {direction}")

    insert_loadsheet((
        str(fdate), flight, total_pax, cargo_total,
        ZFW, TOW, LW, index_val, cg, f"{abs(stab)} {direction}"
    ))

    st.success("Saved")
