import streamlit as st
import pandas as pd
import time

from db.base import get_diagnostics
from ui.utils import process_data

# Set page title
st.set_page_config(page_title="System Diagnostic Metrics", layout="wide")


def create_ui():
    st.markdown("## 🖥️ System Diagnostic Metrics (Real-Time)")

    # Create empty placeholders for real-time updates
    col1, col2, col3 = st.columns(3)
    cpu_chart = col1.empty()
    memory_chart = col2.empty()
    disk_chart = col3.empty()

    st.markdown("### 📄 Last 10 records")
    data_table = st.empty()

    while True:
        # Fetch latest system data
        res = get_diagnostics(10)
        processed_data = process_data(res)  # Ensure data is processed properly

        df = pd.DataFrame(processed_data)
        if not df.empty:
            df["timestamp"] = pd.to_datetime(df["timestamp"])

            # Update charts dynamically
            cpu_chart.line_chart(df.set_index("timestamp")["cpu_usage"], use_container_width=True)
            memory_chart.line_chart(df.set_index("timestamp")["memory_usage"], use_container_width=True)
            disk_chart.line_chart(df.set_index("timestamp")["disk_usage"], use_container_width=True)

            # Update table dynamically
            data_table.dataframe(df, hide_index=True)

            time.sleep(5)  # Update every 2 seconds
            st.rerun()  # Refresh the UI
