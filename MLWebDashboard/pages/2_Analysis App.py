# Import libraries
import ast
import pickle
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.graph_objects as go

# Page title
st.set_page_config(page_title='Analysis')
st.title('Analytics')

# Import all the datasets
df = pd.read_csv('datasets/data_viz1.csv')
wordcloud_df = pickle.load(open('pickles/wordcloud_df.pkl', 'rb'))

# Data preprocessing for geomap designing
group_df = df.groupby('sector').mean()[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']]

st.markdown("<br> <div style='border: 1px solid #ff4d4d'></div>", unsafe_allow_html=True)

# GeoMap
st.subheader('GeoMap')
plt.rcParams['font.family'] = 'Arial'
fig = px.scatter_mapbox(group_df, lat='latitude', lon='longitude', size='built_up_area', color='price_per_sqft', zoom=10, color_continuous_scale=px.colors.cyclical.IceFire, mapbox_style='open-street-map', width=1200, height=700, hover_name=group_df.index)
st.plotly_chart(fig, use_container_width=True)

st.markdown("<br> <div style='border: 0.5px solid #D3D3D3'></div> <br>", unsafe_allow_html=True)

# Wordcloud
st.subheader('Wordcloud')
selected_sector_cloud = st.selectbox('Select a Sector', wordcloud_df['sector'].unique().tolist())
new_cloud = wordcloud_df[wordcloud_df['sector'] == selected_sector_cloud]

wordcloud_text = []
for item in new_cloud['features'].apply(ast.literal_eval):
    wordcloud_text.extend(item)

feature_texts = ' '.join(wordcloud_text)

wordcloud = WordCloud(width=1200, height=800, background_color='white', stopwords={'s'}, min_font_size=10).generate(feature_texts)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis = 'off'
plt.tight_layout(pad=0)
st.pyplot(plt)

st.markdown("<br> <div style='border: 0.5px solid #D3D3D3'></div> <br>", unsafe_allow_html=True)

# Area vs Price
st.subheader('Area Vs Price')
property_type = st.selectbox('Select Property Type', ['flat', 'house'])
fig1 = px.scatter(df[df['property_type']==property_type], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price", animation_frame='agePossession')
st.plotly_chart(fig1, use_container_width=True)

st.markdown("<br> <div style='border: 0.5px solid #D3D3D3'></div> <br>", unsafe_allow_html=True)

# BHK Pie Chart
st.subheader('BHK Pie Chart')
sector_options = df['sector'].unique().tolist()
sector_options.insert(0, 'Overall')
selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'Overall':
    fig2 = px.pie(df, names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(df[df['sector'] == selected_sector], names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("<br> <div style='border: 0.5px solid #D3D3D3'></div> <br>", unsafe_allow_html=True)

# BHK Comparison
st.subheader('Side by Side BHK Comparison')
fig_box = px.box(df[df['bedRoom'] <= 5], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig_box, use_container_width=True)

st.markdown("<br> <div style='border: 0.5px solid #D3D3D3'></div> <br>", unsafe_allow_html=True)

st.header('Side by Side Distplot for Property Type')
# Create histograms for House and Flat with adjusted bin size and bar thickness
hist_house = go.Histogram(x=df[df['property_type'] == 'house']['price'], nbinsx=100, name='house', opacity=0.6, marker=dict(color='blue', line=dict(color='white', width=0.5)))
hist_flat = go.Histogram(x=df[df['property_type'] == 'flat']['price'], nbinsx=100, name='flat', opacity=0.6, marker=dict(color='orange', line=dict(color='white', width=0.5)))

# Create subplot with two histograms
fig_distplot = go.Figure(data=[hist_house, hist_flat], layout=go.Layout(barmode='overlay', title='Price Distribution by Property Type'))
fig_distplot.update_layout(showlegend=True)

st.plotly_chart(fig_distplot, use_container_width=True)


