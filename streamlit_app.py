import streamlit as st
import pandas as pd


@st.cache
def get_electricity_data():
    _df = pd.read_excel("data/IEA_Energy_Prices_Monthly_Excerpt_122022.xlsx", sheet_name="raw_data")
    return _df


df = get_electricity_data()

product_type = st.selectbox("Product type:", options=df['PRODUCT'].unique())
single_country = st.selectbox("Select country:", options=df['COUNTRY'].unique())
multiple_countries = st.multiselect("Select countries:", options=df['COUNTRY'].unique())


st.write(df)
