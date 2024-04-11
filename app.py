import streamlit as st
import src.answers as asw
from src.extraction import load_data

st.set_page_config(layout="wide")

def create_answers_section(df):
    st.title("Main questions Answers")

    st.header("First Round")
    st.subheader("How many bikes are being sold by their owners and how many bikes are being sold by distributors?")

    st.subheader("How many bikes are being sold by their owners and how many bikes are being sold by distributors?")

    st.subheader("How many bikes are being sold by their owners and how many bikes are being sold by distributors?")

    st.subheader("How many bikes being sold are bikes from a unique owner?")

    st.subheader("Are high kilometer bikes more expensive than bikes with lower kilometer counts?")

    st.subheader("Are the bikes with a unique owner more expensive on average than the other bikes?")

    st.subheader("Are the bikes that have had more owners also the bikes with more kilometers traveled on average?")

    st.subheader("Which company has the most bikes registered?")

    st.subheader("Which company has the most expensive bikes on average?")

    st.subheader("Is the company that has the most expensive bikes registered also the company that has the most bikes registered?")

    st.subheader("Which bikes are good purchase choices?")

    return None
 

def create_dataframe_section(df):
    st.title("Database Section")

    col_1, col_2 = st.columns(2)

    col_1.header("Database")
    col_1.dataframe(df, height=530)

    col_2.header("Data Description")

    data_description = """
                        | Column | Description |
                        | :----- | :---------- |
                        | ID | Line/Registry identifier|
                        | name | New model maker |
                        | selling_price | Selling Price |
                        | year | Motorbike's manufacturing year |
                        | seller_type | Type of seller, if it's personal or a reseller |
                        | owner | If it's the first, second, third, or fourth owner of the vehicle |
                        | km_driven | Number of kilometers driven by the vehicle |
                        | ex_showroom_price | Price of the motorbike, excluding taxes, insurance and registry fees|
                        | age | Amount of years the vehicle has been in use for |
                        | km_class | Classification assignet to the motorbike based on kilometers driven |
                        | km_per_year | Amount of kilometers driven per year |
                        | km_per_month | Amount of kilometers driven per month |
                        | company | Manufacturer of the motorbike |
    """
    col_2.markdown(data_description)




def main():
    df = load_data()

    create_dataframe_section(df)

    create_answers_section(df)

    st.dataframe(df)

    return None

if __name__ == '__main__':
    main()
