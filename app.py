import pandas as pd
import streamlit as st
import plotly.express as px
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Restaurant Geo Analytics Dashboard",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3, h4 {
    color: white;
}

.stMetric {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------

df = pd.read_csv("Dataset.csv", encoding='latin-1')

# ---------------- CLEAN DATA ----------------

df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

# ---------------- HEADER ----------------

st.markdown("""
# 🍽 Restaurant Geo Analytics Dashboard

### Analyze restaurant trends, ratings, cuisines and geographical insights.
""")

# ---------------- SIDEBAR ----------------

st.sidebar.header("Dashboard Filters")

selected_city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(df['City'].dropna().unique())
)

if selected_city != "All":
    filtered_df = df[df['City'] == selected_city]
else:
    filtered_df = df

# ---------------- KPI SECTION ----------------

st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Restaurants",
    len(filtered_df)
)

col2.metric(
    "Average Rating",
    round(filtered_df['Aggregate rating'].mean(), 2)
)

col3.metric(
    "Average Cost",
    round(filtered_df['Average Cost for two'].mean(), 0)
)

col4.metric(
    "Countries Covered",
    filtered_df['Country Code'].nunique()
)

# ---------------- HEATMAP ----------------

st.subheader("🌍 Restaurant Heatmap")

map_center = [
    filtered_df['Latitude'].mean(),
    filtered_df['Longitude'].mean()
]

m = folium.Map(
    location=map_center,
    zoom_start=5
)

heat_data = filtered_df[['Latitude', 'Longitude']].values.tolist()

HeatMap(heat_data).add_to(m)

st_folium(m, width=1200, height=500)

# ---------------- TOP CITIES ----------------

st.subheader("🏙 Top Cities with Highest Restaurants")

top_cities = (
    df['City']
    .value_counts()
    .head(10)
    .reset_index()
)

top_cities.columns = ['City', 'Count']

fig1 = px.bar(
    top_cities,
    x='City',
    y='Count',
    title='Top Restaurant Cities',
    template='plotly_dark'
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- RATING DISTRIBUTION ----------------

st.subheader("⭐ Rating Distribution")

fig2 = px.histogram(
    filtered_df,
    x='Aggregate rating',
    nbins=20,
    title='Restaurant Rating Distribution',
    template='plotly_dark'
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- COST VS RATING ----------------

st.subheader("💰 Cost vs Rating Analysis")

fig3 = px.scatter(
    filtered_df,
    x='Average Cost for two',
    y='Aggregate rating',
    hover_name='Restaurant Name',
    size='Votes',
    title='Cost vs Ratings',
    template='plotly_dark'
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- CUISINE ANALYSIS ----------------

st.subheader("🍜 Most Popular Cuisines")

cuisine_data = (
    filtered_df['Cuisines']
    .dropna()
    .str.split(',')
    .explode()
    .str.strip()
)

top_cuisines = cuisine_data.value_counts().head(10)

fig4 = px.pie(
    names=top_cuisines.index,
    values=top_cuisines.values,
    title='Cuisine Popularity',
    template='plotly_dark'
)

st.plotly_chart(fig4, use_container_width=True)

# ---------------- ONLINE DELIVERY ----------------

st.subheader("🚚 Online Delivery Availability")

delivery_counts = filtered_df['Has Online delivery'].value_counts()

fig5 = px.pie(
    names=delivery_counts.index,
    values=delivery_counts.values,
    title='Online Delivery',
    template='plotly_dark'
)

st.plotly_chart(fig5, use_container_width=True)

# ---------------- DATASET TABLE ----------------

st.subheader("📋 Restaurant Dataset")

st.dataframe(filtered_df.head(100))

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    "Developed by Vishal Kumar | Cognifyz Technologies Internship Project"
)