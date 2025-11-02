import streamlit as st
import crop_recommendation
import yield_prediction

st.set_page_config(page_title="AgriSmart Dashboard", page_icon="🌾", layout="centered")

st.sidebar.title("🌿 AgriSmart Menu")
page = st.sidebar.radio("Choose a module:", ["Crop Recommendation", "Crop Yield Prediction"])

if page == "Crop Recommendation":
    crop_recommendation.show_recommendation_page()

elif page == "Crop Yield Prediction":
    yield_prediction.show_yield_page()
