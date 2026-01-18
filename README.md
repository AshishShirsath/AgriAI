**🌾 KrishiSetu – Intelligent Agriculture Assistant**

Team Project | Transformers • CNN • Machine Learning • Clustering • Data Visualization

KrishiSetu is an AI-powered agriculture assistant designed to support farmers, researchers, and policymakers with crop-related insights, predictions, and interactive analytics. The project integrates NLP-based chatbots, machine learning models, and data visualization dashboards into a unified system.

**🚀 Project Overview**

KrishiSetu combines modern Transformer-based NLP, machine learning prediction models, and visual analytics to:

Answer agriculture-related queries via a chatbot

Predict crop yield and recommend suitable crops

Analyze crop production trends across regions and seasons

Provide detailed AI-generated explanations when required

🧠 Key Features
**🤖 Agriculture Chatbot**

Built using Transformer model: MiniLM-L6-v2

Fine-tuned on a custom dataset AgriQA containing 175,000 agriculture-related queries sourced from Hugging Face

Deployed using Gradio on Hugging Face Spaces

Handles queries related to crops, soil, seasons, yield, and farming practices

**🌱 Crop Yield Prediction & Recommendation**

Developed machine learning models using Kaggle agriculture datasets

Predicts:

Crop yield

Suitable crops based on environmental and regional factors

Uses classical ML techniques and clustering for insights and recommendations

**📊 Data Visualization Dashboard**

Created interactive Plotly dashboards

Visualizes:

Crop production trends

Yield variations

Revenue distribution

Allows analysis by region, season, and crop type

**🔗 Backend Integration**

Implemented a Flask backend to:

Connect the chatbot with ML prediction models

Serve interactive visual dashboards

Manage data flow between components

**📖 “Read More” Intelligent Expansion**

Added a Read More feature for complex or incomplete chatbot responses

Automatically forwards queries to an NVIDIA LLM backend

Provides detailed, context-rich answers when the primary chatbot confidence is low


**Tech Stack:**

| Category         | Technologies                   |
| ---------------- | ------------------------------ |
| NLP              | Transformers, MiniLM-L6-v2     |
| Machine Learning | Scikit-learn, CNNs, Clustering |
| Backend          | Flask                          |
| Frontend / UI    | Gradio                         |
| Visualization    | Plotly                         |
| Deployment       | Hugging Face Spaces            |
| LLM Backend      | NVIDIA LLM                     |
