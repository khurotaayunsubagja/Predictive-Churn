import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import timedelta, datetime
import matplotlib.pyplot as plt


# Set page config
st.set_page_config(
    page_title="Statistic",
    page_icon="📊",
)

st.title("Here some overview of data!")

@st.cache_data
def load_data():
    data  = pd.read_csv("Dataset.csv")
    return data

df = load_data()

st.subheader("Demographic")

## df["churn"].sum() otomatis menghitung jumlah 1 (karena 0 tidak menambah apa-apa).
## variabel churn tidak ada yg missing value

total_customer = len(df)              
total_churn = df["Churn"].sum()        
total_non_churn = total_customer - total_churn  
churn_rate = (total_churn / total_customer) * 100 

col1, col2, col3, col4 = st.columns(4)

# --- KPI 1: Views ---
with col1:
    st.metric(label="Churn Customer", value=f"{churn_rate:.2f}%")
with col2 :
    churn_count = df[df["Churn"] == 1]["Gender"].value_counts()

    fig, ax = plt.subplots()
    ax.pie(
        churn_count,
        labels=churn_count.index,
        autopct="%.1f%%",
        startangle=90
    )
    ax.set_title("Churn Distribution by Gender")

    st.pyplot(fig)

    print(df.head())
print(df.columns)
