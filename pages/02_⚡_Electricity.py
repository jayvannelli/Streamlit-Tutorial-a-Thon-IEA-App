import streamlit as st
import pandas as pd


@st.cache
def get_electricity_data():
    _df = pd.read_csv("data/MES_0922.csv", encoding="utf-8", skiprows=8)
    return _df


df = get_electricity_data()


def main():
    st.write(df)


if __name__ == "__main__":
    main()
