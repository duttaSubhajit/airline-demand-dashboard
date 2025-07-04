import streamlit as st
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# Function to fetch Google Trends data
def get_trend_data(keyword):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([keyword], cat=0, timeframe='today 3-m')
    data = pytrends.interest_over_time()
    if not data.empty:
        data.reset_index(inplace=True)
        return data[['date', keyword]]
    else:
        return pd.DataFrame()

# Function to generate static insights (no OpenAI needed)
def generate_insights(data, keyword):
    if data.empty:
        return "No sufficient data to generate insights."

    max_value = data[keyword].max()
    min_value = data[keyword].min()
    latest_value = data[keyword].iloc[-1]

    insights = (
        f"The search demand for {keyword} has fluctuated between {min_value} and {max_value} over the past 3 months. "
        f"The latest demand index is {latest_value}. Consider monitoring this trend for any sudden increases in demand."
    )

    return insights

# Streamlit App
st.set_page_config(page_title="Airline Demand Trends", layout="wide")
st.title("✈️ Airline Booking Market Demand Dashboard")

col1, col2 = st.columns(2)

with col1:
    origin = st.text_input("Enter Origin City", "Sydney")

with col2:
    destination = st.text_input("Enter Destination City", "Melbourne")

keyword = f"Flights from {origin} to {destination}"

if st.button("Get Market Demand"):

    with st.spinner("Fetching data..."):
        trend_data = get_trend_data(keyword)

    if not trend_data.empty:
        st.subheader("📈 Demand Trend Chart")

        fig, ax = plt.subplots()
        ax.plot(trend_data['date'], trend_data[keyword], marker='o')
        ax.set_title(f"Search Trend for {keyword}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Interest Over Time")
        plt.xticks(rotation=45)
        st.pyplot(fig)

        st.subheader("🔍 Insights")

        try:
            insights = generate_insights(trend_data, keyword)
            st.write(insights)
        except Exception:
            st.error("⚠️ Unable to generate insights at the moment.")

        st.subheader("📊 Raw Data")
        st.dataframe(trend_data)

    else:
        st.error("No trend data available for the selected route. Please try different cities.")

st.markdown("---")
st.caption("Powered by Google Trends")

