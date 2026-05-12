import streamlit as st
import json
import time

st.title("🔥 CyberShield AI LIVE SOC DASHBOARD")

placeholder = st.empty()

while True:
    try:
        with open("realtime/live_data.json", "r") as f:
            data = json.load(f)

        placeholder.metric("Active Attacks", data["attacks"])
        st.write("Last IP:", data["ip"])
        st.write("Status:", data["status"])

    except:
        st.write("Waiting for data...")

    time.sleep(1)