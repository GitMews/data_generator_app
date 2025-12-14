# Imports
import streamlit as st
from data_generator import compute_dataframe
from datetime import datetime

# Setup page configuration
st.set_page_config(page_title= "Data Generator App", layout= "centered", page_icon="🌐")

# Metadata
st.title("CSV Generator 💾")
st.write("Compute, generate and download time-series CSV data")
st.text("").markdown("---")

# Parameters
with st.sidebar:
    st.subheader("Parameters ⚙️")
    st.sidebar.markdown("---")
    measure_name = st.text_input("Measure name", value= "Q_RHONE")
    frequency_minuts = st.radio(label= "Frequency (minuts)", options= [1, 15, 60], index= 1)
    duration_hours = st.slider(label="Time duration (hours)", min_value= 1, max_value= 24, value=12)
    datetime_start = st.datetime_input(label= "Datetime start")

# Dataframe preview
dataframe = compute_dataframe(measure_name, frequency_minuts, duration_hours, datetime_start)
st.dataframe(data= dataframe)

# Options : Download or rerun
rerun_button, download_button = st.columns(2)

with rerun_button:
    if st.button("Rerun 🔁"):
        st.rerun()

with download_button:
    csv_data = dataframe.to_csv(index=False).encode("utf-8")
    file_name = f"generated_data_{datetime.now().strftime('%Y_%m_%d_%Hh%M')}.csv"
    st.download_button(label= "Download ⬇️", data= csv_data, file_name= file_name)