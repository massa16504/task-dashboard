import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from io import BytesIO


st.set_page_config(page_title="Task Dashboard", layout="wide")
st.title("📊 Task Dashboard — Harsha Tab")

uploaded_file = st.file_uploader("📤 Upload updated Excel sheet", type=["xlsx"])

if uploaded_file:
    try:
    # Load sheet without headers
    raw_df = pd.read_excel(uploaded_file, sheet_name="Harsha", header=None)
    
    # Normalize column names for matching
    normalized = lambda x: str(x).strip().lower().replace("\n", " ")
    
    # Define required columns
    required = ['status', 'target date', 'task']
    header_row_idx = None
    
    # Scan first 10 rows for potential header
    for i in range(min(10, len(raw_df))):
        row = raw_df.iloc[i].map(normalized).tolist()
        if all(col in row for col in required):
            header_row_idx = i
            break
    
    if header_row_idx is None:
        st.error("❌ Could not detect proper header row. Please make sure the sheet has the required columns.")
    else:
        df = pd.read_excel(uploaded_file, sheet_name="Harsha", header=header_row_idx)
        df.columns = df.columns.str.strip().str.lower().str.replace("\n", " ")
            df.columns = df.columns.str.strip().str.lower().str.replace("\n", " ")

        st.write("🧼 Columns:", df.columns.tolist())

        required = ['status', 'target date', 'task']
        if not all(col in df.columns for col in required):
            st.error(f"Missing required columns: {required}")
        else:
            df['target date'] = pd.to_datetime(df['target date'], errors='coerce')

            total = len(df)
            completed = len(df[df['status'].str.lower() == 'completed'])
            in_progress = len(df[df['status'].str.lower() == 'in progress'])
            not_started = len(df[df['status'].str.lower() == 'not started'])
            overdue = len(df[(df['status'].str.lower() != 'completed') & (df['target date'] < datetime.today())])

            col1, col2, col3, col4, col5 = st.columns(5)
            col1.metric("📋 Total", total)
            col2.metric("✅ Completed", completed)
            col3.metric("🚧 In Progress", in_progress)
            col4.metric("⏳ Not Started", not_started)
            col5.metric("⚠️ Overdue", overdue)

            st.markdown("---")
            st.subheader("📌 Task Distribution by Status")
            chart = px.pie(df, names="status", title="Task Status Breakdown", hole=0.4)
            st.plotly_chart(chart, use_container_width=True)

            st.subheader("🗂 Preview")
            st.dataframe(df.head(10))
    except Exception as e:
        st.error(f"❌ Error: {e}")
else:
    st.info("Please upload an Excel file with a 'Harsha' tab to begin.")
