
Chicago Crime Data Analysis (2010–2019)

This project fetches, cleans, and analyzes public crime data from the [City of Chicago's data portal](https://data.cityofchicago.org/), focusing on the years 2010 through 2019. The analysis outputs structured CSV files summarizing crime by various dimensions like year, time of day, ward, and FBI classification.

📁 Project Structure

- `data/` — exported CSV files  
- `notebooks/` — (optional) Jupyter notebooks  
- `src/`  
  - `fetch.py`  
  - `processing.py`  
  - `main.py`  
- `.gitignore`  
- `README.md`  
- `requirements.txt`

📌 Key Features
📅 Temporal Analysis: Monthly and yearly crime counts.

🕵️ Crime Type Distribution: Trends in theft, assault, burglary, and other categories.

📍 Geographic Insights (Tableau only): Visual breakdowns by location.

📈 Data Aggregation: Grouped statistics for trend analysis using pandas.

📊 Tableau Dashboard
Check out the interactive Tableau dashboard here:

🔗 https://public.tableau.com/app/profile/sergio.castaneda/viz/Analysis_Chicago_Crimes/Analysis_Chicago

Data Source
This project uses open data from the City of Chicago:

Chicago Crime API (Socrata)

Data includes:

Date and time of reported crimes

Primary crime type

Arrests and domestic involvement

Location descriptions (e.g., street, alley, apartment)


Example Insights
Seasonal trends: Crime rates peak during summer months.

Theft is the most common crime, followed by battery and criminal damage.

Year-over-year trends indicate a decrease in overall reported crime after 2016.

Future Improvements
Add geospatial analysis using Folium or Plotly.

Integrate with Streamlit for an interactive Python dashboard.

Automate data updates via API.

Implement predictive modeling to forecast crime trends.

About the Author
Sergio Castaneda
Data Enthusiast | Python & Tableau










