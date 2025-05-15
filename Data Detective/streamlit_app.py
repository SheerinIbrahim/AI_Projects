import streamlit as st
import pandas as pd
from logic import (
    load_dataset,
    descriptive_stats,
    plot_distribution,
    plor_boxplot,
    plot_corr_heatmap,
    plot_pairplot,
)

st.set_page_config(page_title="Data Detective", layout="wide")
st.title("🕵️‍♂️ Data Detective - EDA Tool")

file = st.file_uploader("📂 Upload a CSV file", type=["csv"])
if file:
    df = load_dataset(file)
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    if st.checkbox("📊 Show Descriptive Stats"):
        summary = descriptive_stats(df)
        st.dataframe(summary)

    if st.checkbox("📈 Show Distribution Plots"):
        num_cols = df.select_dtypes(include='number').columns.tolist()
        plot_distribution(df, num_cols)

    if st.checkbox("📦 Show Boxplot"):
        col = st.selectbox("Select column for boxplot", df.columns)
        plor_boxplot(df, col)

    if st.checkbox("🧊 Show Correlation Heatmap"):
        plot_corr_heatmap(df)

    if st.checkbox("👯‍♂️ Show Pairplot (slow on large data)"):
        plot_pairplot(df)
