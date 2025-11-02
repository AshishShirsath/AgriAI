import streamlit as st
import pandas as pd
import joblib
import concurrent.futures

# ---------- GLOBAL THREAD EXECUTOR ----------
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

# ---------- CACHE MODEL LOAD ----------
@st.cache_resource
def load_model():
    """Load the trained crop yield model once and reuse."""
    model = joblib.load("crop_yield_model.pkl")
    return model

# ---------- ASYNC PREDICTION ----------
def predict_async(model, input_data):
    """Run model.predict in a separate thread."""
    return executor.submit(model.predict, input_data)

# ---------- STREAMLIT PAGE ----------
def show_yield_page():
    st.title("🌾 Crop Yield Prediction")
    st.write("Enter agricultural and weather parameters to predict expected yield:")

    model = load_model()

    regions = ['North', 'South', 'East', 'West']
    soil_types = ['Loamy', 'Sandy', 'Clay', 'Silty']
    crops = ['rice', 'maize', 'wheat', 'mango', 'cotton', 'coffee']
    weather_conditions = ['Sunny', 'Rainy', 'Cloudy', 'Stormy']

    col1, col2 = st.columns(2)
    with col1:
        region = st.selectbox("Region", regions)
        soil_type = st.selectbox("Soil Type", soil_types)
        crop = st.selectbox("Crop", crops)
        rainfall_mm = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0)
        temperature_c = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)

    with col2:
        fertilizer_used = st.number_input("Fertilizer Used (kg/ha)", min_value=0.0, max_value=500.0, value=100.0)
        irrigation_used = st.number_input("Irrigation Used (mm)", min_value=0.0, max_value=500.0, value=50.0)
        weather_condition = st.selectbox("Weather Condition", weather_conditions)
        days_to_harvest = st.number_input("Days to Harvest", min_value=30, max_value=300, value=120)

    if st.button("Predict Yield"):
        input_data = pd.DataFrame([{
            "Region": region,
            "Soil_Type": soil_type,
            "Crop": crop,
            "Rainfall_mm": rainfall_mm,
            "Temperature_Celsius": temperature_c,
            "Fertilizer_Used": fertilizer_used,
            "Irrigation_Used": irrigation_used,
            "Weather_Condition": weather_condition,
            "Days_to_Harvest": days_to_harvest
        }])

        with st.spinner("Predicting yield... please wait"):
            future = predict_async(model, input_data)
            pred = future.result()[0]

        st.success(f"🌾 Estimated Yield: **{pred:.2f} tons/hectare**")


