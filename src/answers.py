from io import BytesIO

import pandas as pd
import plotly.express as px
import streamlit as st


def rd1_question_9(df):
    df_grouped = df[["id", "seller_type"]].groupby("seller_type")

    df_grouped = df_grouped.count().reset_index()

    df_grouped = df_grouped.rename(columns={"id": "count"})

    fig = px.bar(
        df_grouped,
        x="seller_type",
        y="count",
        labels={"seller_type": "Seller Type", "count": "Quantity"},
        color="seller_type",
        text="count",
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd1_question_13(df):
    df_grouped = (
        df.groupby("owner")
        .agg(qty=pd.NamedAgg("id", "count"))
        .sort_values("qty")
        .reset_index()
    )

    fig = px.bar(
        df_grouped,
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
    st.text("As we can see, bikes with higher kilometer-traveled counts are cheaper")

    fig = px.scatter(
        df,
        x="km_driven",
        y="selling_price",
        labels={"km_driven": "Kilometers", "selling_price": "Selling Price"},
    )

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd2_question_1(df):
    df_grouped = df.groupby("owner")

    df_grouped = (
        df_grouped.agg(
            avg_price=pd.NamedAgg("selling_price", "mean"),
            qty=pd.NamedAgg("owner", "count"),
        )
        .sort_values("avg_price", ascending=False)
        .reset_index()
    )

    df_grouped["avg_price"] = df_grouped["avg_price"].round(2)

    fig = px.bar(
        df_grouped,
        x="owner",
        y="avg_price",
        labels={"owner": "Owner Types", "avg_price": "Average Price"},
        text="avg_price",
        color="owner",
    )

    fig.update_traces(texttemplate="$ %{text:.2f}", textposition="inside")

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd2_question_2(df):
    df_grouped = df[["owner", "km_driven"]].groupby("owner")

    df_grouped = (
        df_grouped.mean().sort_values("km_driven", ascending=False).reset_index()
    )

    fig = px.bar(
        df_grouped,
        x="owner",
        y="km_driven",
        labels={"owner": "Owner Types", "km_driven": "Average Price"},
        text="km_driven",
        color="owner",
    )

    fig.update_traces(texttemplate="%{text:.2f} Km", textposition="inside")

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd2_question_3(df):
    df_grouped = df[["owner", "age"]].groupby("owner")

    df_grouped = df_grouped.mean().sort_values("age", ascending=False).reset_index()

    df_grouped["age"] = df_grouped["age"].astype(int)

    fig = px.bar(
        df_grouped,
        x="owner",
        y="age",
        labels={"owner": "Owner Types", "age": "Average Price"},
        text="age",
        color="owner",
    )

    fig.update_traces(texttemplate="%{text:.0f} Years", textposition="inside")

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd2_question_7(df):
    df_grouped = df.loc[:, ["company", "id"]].groupby("company")

    df_grouped = df_grouped.count().sort_values("id", ascending=False).reset_index()

    fig = px.bar(
        df_grouped,
        x="company",
        y="id",
        labels={"company": "Companies", "id": "Quantity"},
        text="id",
        color="company",
    )

    fig.update_traces(textposition="outside")

    fig.update_xaxes(tickangle=-80)

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd3_question_2(df):
    df_grouped = df[["company", "selling_price"]].groupby("company")

    df_grouped = (
        df_grouped.agg(
            avg_price=pd.NamedAgg("selling_price", "mean"),
            median_price=pd.NamedAgg("selling_price", "median"),
            std_price=pd.NamedAgg("selling_price", "std"),
            qty=pd.NamedAgg("company", "count"),
        )
        .sort_values("avg_price", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        df_grouped,
        x="company",
        y="avg_price",
        labels={"company": "Companies", "avg_price": "Average Price"},
        text="avg_price",
        color="company",
        title="Company Average Price",
    )

    fig.update_traces(texttemplate="$ %{text:.2f}", textposition="outside")

    fig.update_xaxes(tickangle=-80)

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd3_question_5(df):
    df_grouped = df[["id", "selling_price", "company"]].groupby("company")

    df_grouped = df_grouped.agg(
        max_selling_price=pd.NamedAgg("selling_price", "max"),
        quantity=pd.NamedAgg("id", "count"),
    )

    df_grouped = df_grouped.reset_index().sort_values(
        "max_selling_price", ascending=False
    )

    fig = px.scatter(
        df_grouped,
        x="company",
        y="max_selling_price",
        labels={"company": "Company", "max_selling_price": "Selling Price"},
        text="quantity",
        color="quantity",
    )

    fig.update_traces(marker={"size": 20}, textposition="top center")

    fig.update_xaxes(tickangle=-80)

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd3_question_7(df):
    # Filters
    year = df["year"] >= 2018
    venda = df["selling_price"] < df["ex_showroom_price"]
    donos = df["owner"] == "1st owner"
    vendedor = df["seller_type"] == "Individual"
    km_rodado = df["km_driven"] <= 40000

    # Columns
    columns = ["id", "name", "selling_price", "km_driven", "year"]

    # Data Selection
    df_selected = df.loc[
        year & km_rodado & donos & vendedor & venda, columns
    ].sort_values("selling_price", ascending=False)

    st.dataframe(df_selected)

    return None
