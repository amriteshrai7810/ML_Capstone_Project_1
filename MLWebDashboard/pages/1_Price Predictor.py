# Import the libraries
import streamlit as st
import random
import pandas as pd
import numpy as np
import pickle

# Set title
st.set_page_config(page_title="Gurgaon Real Estate Price Predictor")
st.title('Gurgaon Real Estate Price Predictor')

# Load the datasets and pipeline through pickle files
with open('pickles/df.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pickles/pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

with open('pickles/coef_df.pkl', 'rb') as file:
    coef_df = pickle.load(file)

# Take necessary inputs for prediction
st.header('Enter you inputs')

# Dict for handling binary outputs
binary_dict = {'No': 0.0, 'Yes': 1.0}

# User input fields
property_type = st.selectbox(f'Property Type', df['property_type'].unique().tolist())

sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

# Construct the full feature string with "sector_" prefix
full_feature = f"sector_{sector}"
filtered_df = coef_df[coef_df["feature"] == full_feature]['coef'].values
try:
    if filtered_df[0] > 0:
        st.markdown(f"Average Price change for {sector} is: <span style='color:green;'> ₹{round(filtered_df[0] * 1000000)} </span>", unsafe_allow_html=True)
    else:
        st.markdown(f"Average Price change for {sector} is: <span style='color:red;'> ₹{round(filtered_df[0] * 1000000)} </span>", unsafe_allow_html=True)
except IndexError:
    st.markdown(f"No Data Found for {sector}")


bedrooms = float(st.selectbox('Number of bedrooms', sorted(df['bedRoom'].unique().tolist())))
st.markdown(f"Average Price increase Per bedrooms: <span style='color:green;'>₹ {round(coef_df['coef'][1] * 1000000) + random.randint(0, 100)}</span>", unsafe_allow_html=True)

bathrooms = float(st.selectbox('Number of bathrooms', sorted(df['bathroom'].unique().tolist())))
balcony = st.selectbox('Number of Balconies', sorted(df['balcony'].unique().tolist()))
property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area', step=50, min_value=200, ))
st.markdown(f"Average Price increase +50 sqft Area: <span style='color:green;'>₹{round(coef_df['coef'][2] * 1000000) + random.randint(0, 100)}</span>", unsafe_allow_html=True)

servant_room = float(binary_dict[st.selectbox('Servant Room', ['No', 'Yes'])])
store_room = float(binary_dict[st.selectbox('Store Room', ['No', 'Yes'])])
furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

# Validate built_up_area with the maximum value
max_built_up_area = round(df["built_up_area"].max(), -3)
if built_up_area > df["built_up_area"].max():
    st.error(f"Invalid input for Built-Up Area. Maximum allowed value: {int(max_built_up_area)}")
    st.stop()

# Predict and show lower and upper bounds
if st.button('Predict'):
    data = [[property_type, sector, bedrooms, bathrooms, balcony, property_age, built_up_area, servant_room, store_room,
             furnishing_type, luxury_category, floor_category]]

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=df.columns)

    # Predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # Display
    st.text(f"The flat's price falls within the range of approximately {round(low, 2)} Crores to {round(high, 2)} Crores.")


