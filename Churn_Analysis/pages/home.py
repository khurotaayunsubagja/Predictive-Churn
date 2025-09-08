import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏚️",
)

st.title("Welcome to Churn Analysis Dashboard!")

st.markdown("### Hi!👋")
st.write(
    """
    💡 *Did you know that acquiring a new customer can cost five times more than retaining an existing one?*
    Understanding why customers leave is the key to building sustainable business growth.
    """
)
    


st.write("This dashboard is designed to help businesses : ")
st.write(
    """
    - 🔍 Identify customers who are at risk of churning.
    - 📈 Analyze the key factors that influence churn behavior.
    - 🎯 Support strategic decisions to improve customer retention. 
    """
    )


st.markdown("## 🎯 Objective of the Analysis")
st.write("The main objective of this churn analysis is to compare the performance of two machine learning models: XGBoost and LightGBM.")
st.write(
"""
The evaluation is conducted under two conditions:
1. Using datasets *with missing values.*
2. Using datasets *without missing values.*
"""
)

st.markdown("### 📂 Data Source")
st.write("The dataset used in this analysis is sourced from Kaggle, a leading platform for open data and machine learning projects. The dataset contains customer behavior and service usage information, making it well-suited for predictive churn modeling.")

st.write(
    """
Through this comparison, the analysis aims to highlight how each model performs in handling real-world data challenges and to determine the most effective approach for churn prediction.

✨ Use these insights to build stronger customer relationships and ensure sustainable business growth.
"""
)

st.markdown("### 👉 Getting Started:")
st.write("To begin exploring the dashboard, please use the sidebar menu on the left to navigate.")