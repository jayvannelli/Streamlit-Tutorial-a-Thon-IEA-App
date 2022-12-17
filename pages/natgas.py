import streamlit as st
import pandas as pd


@st.cache
def get_electricity_data():
    _df = pd.read_csv("data/natgas.csv")
    return _df


df = get_electricity_data()

st.write(df)
