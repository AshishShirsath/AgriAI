import streamlit as st
import pandas as pd
import joblib

def show_recommendation_page():
    model = joblib.load("crop_recommendation2.pkl")

    label_map = {
        1: 'rice', 2: 'maize', 3: 'chickpea', 4: 'kidneybeans', 5: 'pigeonpeas',
        6: 'mothbeans', 7: 'mungbean', 8: 'blackgram', 9: 'lentil', 10: 'pomegranate',
        11: 'banana', 12: 'mango', 13: 'grapes', 14: 'watermelon', 15: 'muskmelon',
        16: 'apple', 17: 'orange', 18: 'papaya', 19: 'coconut', 20: 'cotton',
        21: 'jute', 22: 'coffee'
    }

    rainfall_map = {'Very High': 1, 'High': 2, 'Medium': 3, 'Low': 4}
    ph_map = {'Neutral': 1, 'Alkaline': 2, 'Acidic': 3}

    st.title("🌱 Crop Recommendation System")
    st.write("Enter soil and weather parameters to get the best crop recommendation:")

    col1, col2, col3 = st.columns(3)
    with col1:
        N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0, value=50.0)
        P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=200.0, value=50.0)
    with col2:
        K = st.number_input("Potassium (K)", min_value=0.0, max_value=200.0, value=50.0)
        temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
    with col3:
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0)

    ph_category = st.selectbox("pH Category", list(ph_map.keys()))
    rainfall_level = st.selectbox("Rainfall Level", list(rainfall_map.keys()))

    if st.button("Predict Crop"):
        try:
            values = {
                "N": N, "P": P, "K": K, "temperature": temperature,
                "humidity": humidity, "ph": 7.0, "rainfall": rainfall
            }

            values["ph_category"] = ph_map[ph_category]
            values["rainfall_level"] = rainfall_map[rainfall_level]
            values["NPK"] = (N + P + K) / 3
            values["THI"] = (temperature * humidity) / 100
            values["temp_rain_interaction"] = temperature * rainfall
            values["ph_rain_interaction"] = values["ph"] * rainfall

            df = pd.DataFrame([values])
            pred = model.predict(df)
            crop = label_map[pred[0]]

            st.success(f"🌾 Recommended Crop: **{crop.upper()}**")

        except Exception as e:
            st.error(f"Error: {e}")
