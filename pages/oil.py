import streamlit as st
import pandas as pd


@st.cache
def get_electricity_data():
    _df = pd.read_csv("data/oil.csv")
    return _df


df = get_electricity_data()

data_type = st.selectbox("Data type:", options=df['DATATYPE'].unique())
single_country = st.selectbox("Select country:", options=df['COUNTRY'].unique())
multiple_countries = st.multiselect("Select countries:", options=df['COUNTRY'].unique())


st.write(df)
