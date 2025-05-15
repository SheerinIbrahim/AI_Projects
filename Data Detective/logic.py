import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_dataset(file_path):
    return pd.read_csv(file_path)

def descriptive_stats(data_frame):
    stats = data_frame.describe(include='all').T
    stats['nulls'] = data_frame.isnull().sum()
    stats['unique'] = data_frame.nunique()
    stats['skew'] = data_frame.skew(numeric_only=True)
    stats['kurtosis'] = data_frame.kurtosis(numeric_only=True)
    return stats

def plot_distribution(data_frame, num_cols):
    import streamlit as st
    for x in num_cols:
        fig, ax = plt.subplots()
        sns.histplot(data_frame[x], kde=True, ax=ax)
        ax.set_title(f'Distribution: {x}')
        st.pyplot(fig)

def plor_boxplot(data_frame, col):
    import streamlit as st
    fig, ax = plt.subplots()
    sns.boxplot(data=data_frame, x=col, ax=ax)
    ax.set_title('Boxplot')
    st.pyplot(fig)

def plot_corr_heatmap(data_frame):
    import streamlit as st
    fig, ax = plt.subplots()
    corr = data_frame.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

def plot_pairplot(data_frame):
    import streamlit as st
    fig = sns.pairplot(data_frame)
    st.pyplot(fig)
