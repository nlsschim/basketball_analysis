import pandas as pd
import streamlit as st

# --- page setup ---

st.write("This page is for loading data.")

# --- data loading ---

data_file = st.file_uploader("Upload a CSV file", type=["csv"])

if data_file:
    st.session_state["data"] = pd.read_csv(data_file)
    st.session_state["data_loaded"] = True
    st.write("Data loaded.")
    st.write(st.session_state["data"].head(5))

st.write(st.session_state["data"].head(10))
    