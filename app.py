import streamlit as st
from src.extraction import load_data

st.set_page_config(layout="wide")

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
    df_raw = load_data()

    create_dataframe_section(df_raw)

    st.dataframe(df_raw)

if __name__ == '__main__':
    main()