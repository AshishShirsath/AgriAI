import streamlit as st
from crop_recommendation import show_recommendation_page
from yield_prediction import show_yield_page

# App Configuration
st.set_page_config(
    page_title="AgriSmart Dashboard",
    page_icon="🌾",
    layout="centered"
)

# Sidebar Navigation
st.sidebar.title("🌿 AgriSmart Menu")
page = st.sidebar.radio("Choose a module:", ["Crop Recommendation", "Crop Yield Prediction"])

# Routing
if page == "Crop Recommendation":
    show_recommendation_page()

elif page == "Crop Yield Prediction":
    show_yield_page()

# Footer (Optional)
st.markdown("---")
st.markdown("**AgriSmart 🌾 | Smart Agriculture Insights**")
