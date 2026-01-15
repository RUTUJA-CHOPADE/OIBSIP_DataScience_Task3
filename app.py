import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("car_price_model.pkl", "rb"))

st.title("🚗 Car Price Prediction App")
st.write("Predict the selling price of a car using Machine Learning")

# User inputs
year = st.number_input("Year of Purchase", min_value=2000, max_value=2025)
present_price = st.number_input("Present Price (in lakhs)", min_value=0.0)
kms_driven = st.number_input("Kilometers Driven", min_value=0)

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
selling_type = st.selectbox("Selling Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# Encoding inputs (must match training)
fuel = 0 if fuel_type == "Petrol" else 1 if fuel_type == "Diesel" else 2
seller = 0 if selling_type == "Dealer" else 1
trans = 0 if transmission == "Manual" else 1

# Predict button
if st.button("Predict Price"):
    input_data = pd.DataFrame(
        [[year, present_price, kms_driven, fuel, seller, trans]],
        columns=["Year", "Present_Price", "Driven_kms", "Fuel_Type", "Selling_type", "Transmission"]
    )
    
  prediction = model.predict(input_data)[0]

# Prevent unrealistic price
prediction = min(prediction, present_price)

st.success(f"Estimated Car Price: ₹ {prediction:.2f} Lakhs")

