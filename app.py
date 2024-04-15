import pandas as pd
import streamlit as st

import src.answers as asw
from src.extraction import load_data

st.set_page_config(layout="wide")


def create_dataframe_section(df):
    st.title("Sections - Database Description")

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
                        | km_traveled | Number of kilometers traveled by the vehicle |
                        | ex_showroom_price | Price of the motorbike, excluding taxes, insurance and registry fees|
                        | age | Amount of years the vehicle has been in use for |
                        | km_class | Classification assignet to the motorbike based on kilometers traveled |
                        | km_per_year | Amount of kilometers traveled per year |
                        | km_per_month | Amount of kilometers traveled per month |
                        | company | Manufacturer of the motorbike |
    """

    col_2.markdown(data_description)


def create_answers_section(df):
    st.title("Main Questions Answers")

    st.header("First Round")
    st.subheader(
        "How many bikes are being sold by their owners and how many bikes are being sold by distributors?"
    )
    asw.rd1_question_9(df)

    st.subheader("How many bikes being sold are from a unique owner?")
    asw.rd1_question_13(df)

    st.subheader(
        "Are bikes with higher kilometer-traveled counts more expensive than bikes with lower ones?"
    )
    asw.rd1_question_14(df)

    st.subheader(
        "Are the bikes with a unique owner more expensive on average than other bikes?"
    )
    asw.rd2_question_1(df)

    st.subheader(
        "Are the bikes that have more owners also the bikes with more kilometers traveled on average?"
    )
    asw.rd2_question_2(df)

    st.subheader("Which company has the most bikes registered?")
    asw.rd2_question_7(df)

    st.subheader("Which company has the most expensive bikes on average?")
    asw.rd3_question_2(df)

    st.subheader(
        "Is the company that has the most expensive bikes registered also the company that has the most bikes registered?"
    )
    asw.rd3_question_5(df)

    st.subheader("Which bikes are good purchase choices?")
    asw.rd3_question_7(df)


def create_main_layout():
    df = load_data()

    create_dataframe_section(df)

    create_answers_section(df)


if __name__ == "__main__":
    create_main_layout()
