# Restaurant Geo Analytics Dashboard

An interactive business intelligence and geographical analytics dashboard developed using Streamlit for analyzing restaurant data, customer trends, cuisines, ratings, pricing, and delivery insights.

This project was developed as part of the Machine Learning Internship Program at Cognifyz Technologies.

---

## Overview

The Restaurant Geo Analytics Dashboard provides detailed analytical insights into restaurant datasets using interactive visualizations and geographical mapping techniques.

The dashboard enables users to:

- Analyze restaurant distribution geographically
- Explore rating patterns and customer trends
- Compare pricing and ratings
- Identify popular cuisines
- Study online delivery availability
- Filter restaurant data city-wise
- Generate business insights through visual analytics

---

## Features

### Geographic Heatmap
Visualizes restaurant density using interactive heatmaps based on latitude and longitude coordinates.

### Key Performance Metrics
Displays:
- Total Restaurants
- Average Rating
- Average Cost for Two
- Countries Covered

### City-Based Filtering
Allows dynamic filtering and exploration of restaurant data for specific cities.

### Rating Distribution Analysis
Provides insights into restaurant rating trends using histogram visualizations.

### Cost vs Rating Analysis
Analyzes the relationship between restaurant pricing and customer ratings.

### Cuisine Popularity Analysis
Displays the most popular cuisines using interactive pie charts.

### Online Delivery Insights
Analyzes the availability of online food delivery services across restaurants.

### Interactive Dataset Viewer
Displays filtered restaurant data in tabular format.

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Pandas | Data Processing and Analysis |
| Streamlit | Interactive Dashboard Development |
| Plotly | Data Visualization |
| Folium | Geographical Mapping |
| Streamlit-Folium | Map Integration in Streamlit |

---

## Project Structure

```plaintext
restaurant-geo-analytics-dashboard/
│
├── app.py
├── Dataset.csv
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/restaurant-geo-analytics-dashboard.git
```

### Navigate to Project Folder

```bash
cd restaurant-geo-analytics-dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```plaintext
http://localhost:8501
```

---

## Dashboard Modules

### Restaurant Heatmap
Interactive geographical visualization of restaurants.

### Business Metrics Dashboard
High-level KPIs for quick analysis.

### Restaurant Analytics
- Ratings Analysis
- Pricing Analysis
- Cuisine Insights
- Delivery Insights

### Data Explorer
Interactive restaurant dataset table.

---

## Dataset Information

The dataset contains:
- Restaurant Names
- Locations
- Latitude & Longitude
- Aggregate Ratings
- Cuisines
- Average Cost
- Online Delivery Availability
- Votes and Reviews
- Country Codes

---

## Learning Outcomes

Through this project, the following concepts were implemented:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis
- Interactive Dashboard Development
- Geospatial Data Visualization
- Business Intelligence Analytics
- Streamlit Application Development

---

## Future Enhancements

Potential future improvements include:

- Machine Learning based restaurant prediction
- Sentiment Analysis on restaurant reviews
- Real-time map clustering
- Recommendation engine integration
- Advanced filtering options
- Deployment on Streamlit Cloud

---

## Author

**Vishal Kumar**

Machine Learning Intern

---

## Internship Organization

Cognifyz Technologies

"Where Data Meets Intelligence"

---

## License

This project is developed for educational and internship purposes.