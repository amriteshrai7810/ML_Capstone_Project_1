# About Gurgaon Real Estate Analysis and Property Price Prediction
This project is built on machine learning algorithms with the aim of assisting individuals looking to purchase properties in Gurgaon. It provides recommendations and predictions for various factors to aid in the decision-making process.
The aim of building this project was to empower buyers by providing them with insights into property prices and facilities, assisting them in making informed decisions

# Video Demo on LinkedIn
LinkedIn Link: [linkedin.com](https://www.linkedin.com/feed/update/urn:li:activity:7171491581231902721/)

# Description
> Model_Development
- It offers a Streamlit web dashboard to assist you in the process of buying properties in Gurgaon
- Price Predictor: This page utilizes Random Forest Regressor and XGBoost to predict property prices based on selected options. It employs linear regression feature importance to estimate changes in variables for different options
- Analysis App: Leveraging GeoMap (Plotly), word clouds, and various charts, this page assists users in analyzing properties and their prices
- Recommend Apartments: This feature suggests similar apartments based on price, facilities, and distance, utilizing a custom function with weighted cosine similarity
	- Image Loader: Utilizing BeautifulSoup and requests, this feature dynamically scrapes and loads images for the recommended apartments

> MlWebDashboard
# EDA & Scraping
- Used Selenium and BeautifulSoup to scrape data from 99acres
- Applied various techniques, including data cleaning, feature engineering, and model building, using Numpy, Pandas, Dtale, Seaborn, Matplotlib, and Scikit-learn

# Run the Project
- Step 1: Run "pip install -r requirements.txt" to install all necessary packages. This command installs the required packages in your Python environment, either globally or locally, based on the context in which the command is executed
- Step 2: Launch the website on your local server by running 'streamlit run Home.py' after navigating to the project directory


# How to use the project
- If you are looking to buy properties in Gurgaon and lack information about costs or suitable areas, or if you are contemplating a move to a new society, this website can provide assistance.
It offers estimates of property costs based on your desired facilities and can recommend similar societies if you are considering relocating to a new location in Gurgaon
