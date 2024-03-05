# Import libraries
import streamlit as st
from PIL import Image

# Configure Streamlit page settings
st.set_page_config(page_title="Real Estate Analytics App")

# Home Page
st.title('Real Estate Analytics App')
st.markdown("---")

# Offer a concise welcome message or introductory note
st.write(""" Welcome to the Real Estate Analytics App! This application aids in analyzing and exploring real estate data in Gurgaon.
 Navigate across pages for price predictions, analytics visualization, and apartment recommendations.""")

# Include an image to enhance visual
image = Image.open("images/real_estate_analysis.jpg")  # Replace with the path to your image
st.image(image, caption="Real Estate Analytics App", use_column_width=True, width=400)

# Include more information or links to help users easily navigate
st.write("Explore the various functionalities by selecting the pages from the sidebar.")

st.markdown("---")

# price Prediction description
st.header("Price Prediction")
st.write("The Gurgaon property price prediction algorithm utilizes machine learning, leveraging crucial factors such as "
         "location, amenities, and market trends for rapid and highly accurate property price estimates")

st.page_link("http://localhost:8501/Price_Predictor", label="Price_Predictor", icon="💰")

# Analysis App description
st.header("Analysis App")
st.write("Effortlessly explore Gurgaon properties with our data analysis app, backed by machine learning and advanced Python. "
         "Gain valuable insights for informed real estate decisions")
st.page_link("http://localhost:8501/Analysis_App", label="Analysis App", icon="🔍")

# Recommend Apartments description
st.header("Recommend Apartments")
st.write("Explore your perfect Gurgaon property with our AI-powered recommendation system. "
         "Personalized suggestions, considering location, landmarks, and societies, ensure efficient real estate choices")

st.page_link("http://localhost:8501/Recommend_Apartments", label="Recommend Apartments", icon="🤝")

st.markdown("---")
st.write("Contact: amriteshrai7180@gmail.com")