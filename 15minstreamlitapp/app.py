import pandas as pd
import streamlit as st
# import metaplotlib.pyplot as plt

st.title("SIMPLE DATA DASHBOARD")
file_uploader = st.file_uploader("Upload CSV", type=["csv"])
# Main Condition of whole project
if file_uploader is not None:
    st.spinner()
    data_frame= pd.read_csv(file_uploader)
    st.subheader("DATA PREVIEW")
    st.write(data_frame.head())
    st.subheader("DATA SUMMARY")
    st.write(data_frame.describe())
    
    st.subheader("Filter DATA")
    columns = data_frame.columns.tolist()
    selected_column = st.selectbox("Select Column", columns)
    unique_value = data_frame[selected_column].unique()
    selected_value = st.selectbox("Select Value", unique_value)

    filtered_data_frame = data_frame[data_frame[selected_column] == selected_value]
    st.write(filtered_data_frame)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X Column", columns)
    y_column = st.selectbox("Select Y Column", columns)
    if st.button("Plot Graph"):
        st.bar_chart(filtered_data_frame.set_index(x_column)[y_column])
else:
    st.write("Please upload a CSV file to proceed.")
