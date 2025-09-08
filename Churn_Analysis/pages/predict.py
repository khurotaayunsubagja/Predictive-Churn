import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Predictive",
    page_icon="🧮",
)

st.title("Let's Try to Predict Your Data!")


# --- Load models ---
xgb_model = joblib.load("xgb_model.joblib")
lgbm_model = joblib.load("lgb_model.joblib")
encoders = joblib.load("manual_encoders.joblib")
model_scores = joblib.load("model_scores.joblib") 


st.markdown("## Churn Prediction Form")
st.write("Please input customer information to predict churn probability:")

# --- Model Selector ---
selected_model_name = st.selectbox("Select Model", ["XGBoost", "LightGBM"])


# Buat 2 kolom
col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (Months)", min_value=0, step=1)
    preferred_device = st.selectbox("Preferred Login Device", ["Mobile Phone", "Computer"])
    city_tier = st.selectbox("City Tier", [1, 2, 3])
    warehouse_to_home = st.number_input("Warehouse to Home (KM)", min_value=0.0, step=0.1)
    payment_mode = st.selectbox("Preferred Payment Mode", ["Credit Card", "Debit Card", "UPI", "E-Wallet", "COD"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    hours_spent = st.number_input("Hours Spent on App", min_value=0.0, step=0.1)
    devices_registered = st.number_input("Number of Devices Registered", min_value=1, step=1)
    cashback_amount = st.slider("Cashback Amount", 1, 5, 3)

with col2:
    order_category = st.selectbox("Preferred Order Category", ["Laptop & Accessory", "Fashion", "Mobile Phone","Grocery"])
    satisfaction_score = st.slider("Satisfaction Score", 1, 10, 5)
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
    num_address = st.number_input("Number of Address", min_value=1, step=1)
    complain = st.selectbox("Complain (1=Yes, 0=No)", [0, 1])
    order_hike = st.number_input("Order Amount Hike From Last Year (%)", min_value=0, step=1)
    coupun_used = st.slider("Coupun Used", 1, 5, 3)
    order_count = st.number_input("Order Count", min_value=1, step=1)
    days_last_order = st.number_input("Days Last Order", min_value=1, step=1)
    # Tambah field lainnya di sini kalau masih ada


# --- Build Input DataFrame ---
input_data = pd.DataFrame([{
    "Tenure": tenure,
    "Preferred Login Device": preferred_device,
    "City Tier": city_tier,
    "Warehouse to Home": warehouse_to_home,
    "Preferred Payment Mode": payment_mode,
    "Gender": gender,
    "Hour Spend On App": hours_spent,
    "Number of Device Registered": devices_registered,
    "Prefered Order Category": order_category,
    "Satisfaction Score": satisfaction_score,
    "Marital Status": marital_status,
    "Number of Address": num_address,
    "Complain": complain,
    "Order Amount Hike from Last Year": order_hike,
    "Coupon Used": coupun_used,
    "Order Count": order_count,
    "Day Since Last Order": days_last_order,
    "Cashback Amount": cashback_amount
}])


# --- Prediction ---
if st.button("🔍 Predict Churn"):
    # Transform input user pakai encoder yang sama
    for col in encoders:
        input_data[col] = encoders[col].transform(input_data[col].astype(str))
    
    # Pilih model sesuai selectbox
    if selected_model_name == "XGBoost":
        model = xgb_model
    else:
        model = lgbm_model
    
    # Prediksi
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    accuracy = model_scores[selected_model_name]

    st.info(f"📊 Using **{selected_model_name}** model (Accuracy: {accuracy*100:.2f}%)")
    st.success(f"📌 Hasil Prediksi: {prediction} (Probabilitas churn: {probability:.2f})")





