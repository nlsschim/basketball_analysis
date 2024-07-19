import streamlit as st
import pandas as pd

# --- page setup ---



about_page = st.Page(
    title="About",
    icon="ℹ️",
    page="views/about.py",
    default=True
)

data_page = st.Page(
    title="Data Loading",
    page="views/data_loading.py",
    icon="📊",
)

plot_one_page = st.Page(
    title="Plot One",
    page="views/plot_one.py",
    icon="📈",
)

plot_one_two = st.Page(
    title="Plot Two",
    page="views/plot_two.py",
    icon="📈",
)

if "data" not in st.session_state:
    st.session_state["data"] = None

if "data_loaded" not in st.session_state:
    st.session_state["data_loaded"] = False




pg = st.navigation(
    {
        "Info": [about_page],
        "Data Loading": [data_page],
        "Data Visualization": [plot_one_page, plot_one_two],
    }
    )

pg.run()
