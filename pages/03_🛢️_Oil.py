import streamlit as st
import pandas as pd


@st.cache
def get_electricity_data():
    _df = pd.read_csv("data/oil.csv")
    return _df


df = get_electricity_data()


def main():
    st.title("Monthly Oil Statistics")
    st.subheader("Monthly oil statistics for OECD countries.")

    st.write("---")
    st.subheader("Overview")
    st.write("""
        This report includes the latest monthly data on oil production for all OECD member 
        countries, and imports, exports, refinery outputs and net deliveries for major 
        product categories for all OECD regions. The publication also includes total oil 
        stock levels and stock changes for major product categories for all OECD member countries. 
        Together with the latest month data are included the last two year and last quarter 
        aggregates, the year-to-date figures for the current and previous year and the year-on-year
         and year-to-date percentage changes.
    """)

    st.write("---")

    continue_on_tab, try_it_yourself_tab = st.tabs(
        ["Continue on...", "Try writing a title, subheader and description yourself"]
    )

    with try_it_yourself_tab:

        with st.form("try_it_yourself_form"):
            title_input = st.text_input("Header", placeholder="Placeholder text for text box...")
            subheader_input = st.text_input("Subheader", placeholder="Placeholder text for text box...")
            long_text_input = st.text_area("Description", placeholder="""You could write a super long placeholder in here because there is so much space to type... 
wow oh wow have I gone past the max line length in python yet.
            """)
            title_and_subheader_data = {
                "titleInput": title_input,
                "subheaderInput": subheader_input,
                "longTextInput": long_text_input,
            }
            try_it_yourself_submit_button = st.form_submit_button("Send!")

        if try_it_yourself_submit_button:
            st.json(title_and_subheader_data)

        st.write("---")
        st.write("Streamlit forms are awesome!")
        with st.expander("Code for above form:"):
            st.code("""
with st.form('try_it_yourself_form'):
    title_input = st.text_input('Header', placeholder='Placeholder text for text box...')
    subheader_input = st.text_input('Subheader', placeholder='Placeholder text for text box...')
    long_text_input = st.text_area('Description', placeholder='You could write a super long placeholder here')

    title_and_subheader_data = {
        "titleInput": title_input,
        "subheaderInput": subheader_input,
        "longTextInput": long_text_input,
    }
    try_it_yourself_submit_button = st.form_submit_button("Send!")
    
    if try_it_yourself_submit_button:
        st.json(title_and_subheader_data)
            """)

    with continue_on_tab:

        st.subheader("How to work with data in Streamlit")
        st.write("""
            Well data can be in many different forms so it completely depends on the source of 
            your data, but for us we have a CSV file downloaded locally in the src/data directory 
            of this project... so we'll use that.
        """)

        with st.expander("Get this data directly from the source"):
            st.write("Link to IEA dataset listing.")
            st.write("https://www.iea.org/data-and-statistics/data-product/monthly-oil-statistics")

        with st.expander("Display code to import and start working with data in streamlit"):
            st.write("")
            st.write("*Its this easy to turn CSV files into fully functional webapps with pandas and streamlit.")

            st.code('''import streamlit as st
import pandas as pd

CSV_FILE_PATH = 'data/oil.csv'

# st.cache is super useful for larger datasets / expensive functions.
@st.cache
def get_data():
    return pd.read_csv(CSV_FILE_PATH)
    
    
df = get_data()
            ''')

        with st.expander("Display data"):
            st.write("")
            st.write("Code to display DataFrame:")
            st.code("""
# get_data() function defined in previous expander.
df = get_data()

st.dataframe(df)
            """)

            st.write("""
                Streamlit allows you work with imported data easily right off the bat.
                Try sorting the DataFrame values by clicking on one the different column names.
            """)
            st.dataframe(df)

        st.write("---")
        st.subheader("Congrats!! You just learned how to work with data from a CSV file.")
        st.write("""
            Now your data is a pandas DataFrame, making it super easy to perform analysis with tools
            like numpy, or just simply utilize the power of pandas!

            Lets say we wanted to get all the data within this dataset pertaining to just a single country.
            We could do that by adding a streamlit selectbox for all unique values in the 'COUNTRY' column.
        """)

        single_country = st.selectbox("Select country:", options=df['COUNTRY'].unique())
        st.write(f"You currently have the value: {single_country} chosen from the selectbox.")

        st.code("""
single_country = st.selectbox("Select country:", options=df['COUNTRY'].unique())

st.write(f"You currently have the value: {single_country} chosen from the selectbox.")
        """)

        st.write("---")

        st.write("""
            Okay that's pretty cool... but what if I want to select multiple countries to compare their values?
            That sounds like just the job for streamlit.multiselect()
        """)

        multiple_countries = st.multiselect(label="Select multiple countries:",
                                            options=df['COUNTRY'].unique(),
                                            default=["DENMARK", "FRANCE", "CANADA"])
        running_country_tally = []
        for country in multiple_countries:
            running_country_tally.append(country)

        st.write("Running country tally:")
        if len(running_country_tally) > 0:
            st.write(running_country_tally)

        st.write("Code for above:")
        st.code("""
multiple_countries = st.multiselect(label="Select multiple countries:", 
                                    options=df['COUNTRY'].unique(),
                                    default=["DENMARK", "FRANCE", "CANADA"])

running_country_tally = []
for country in multiple_countries:
    running_country_tally.append(country)

if len(running_country_tally) > 0:
    st.write(running_country_tally)
        """)

        st.write("---")

        st.write("""
        Now that we have the ability to collect user input using Streamlit widgets, 
        we can use that to transform data with their easy to use charting abilities.
        For this example lets get a simple bar showing data collected for Denmark.
        """)


if __name__ == "__main__":
    main()
