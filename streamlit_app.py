import streamlit as st

st.set_page_config(page_title="IEA Streamlit Dashboard",
                   page_icon=":earth:",
                   layout="centered")


def main():
    st.title("International Energy Agency (IEA) Web-App")
    st.image("images/International-energy-agency-logo.png", width=150)


if __name__ == "__main__":
    main()

