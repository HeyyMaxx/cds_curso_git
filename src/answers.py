import pandas as pd
import plotly.express as px
import streamlit as st


def rd1_question_9(df):
    df_grouped = df[['id', 'seller_type']].groupby('seller_type')

    df_grouped = df_grouped.count().reset_index()

    df_grouped = df_grouped.rename(columns={'id': 'count'})

    fig = px.bar(
        df_grouped,
        x="seller type",
        y="count",
        labels={"seller type": "Seller Type", "count": "Quantity"},
        color="seller_type",
        text="count",
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd1_question_13(df):
    df_grouped = df.groupby('owner').agg(qty = pd.NamedAgg('id', 'count')).sort_values('qty').reset_index()

    fig = px.bar(
        df.grouped,
        x="owner",
        y="qty",
        labels={"owner": "Owner Types", "qty": "Quantity"},
        color="owner",
        text="qty",
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd1_question_14(df):
    st.text("As we can see, bikes with higher kilometer counts have the cheapest prices.")

    fig = px.scatter(
        data = df,
        x = "km_driven",
        y = "selling_price",
        labels={"km_driven": "Kilometers", "selling price": "Selling Price"},
    )

    st.plotly_chart(fig, use_container_width=True)

    return None

