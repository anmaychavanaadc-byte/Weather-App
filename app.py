import streamlit as st
import requests
from datetime import datetime

# Your OpenWeather API Key
API_KEY = st.secrets["OPENWEATHER_API_KEY"]

# Page Configuration
st.set_page_config(
    page_title="Weather App",
    page_icon="🌤️",
    layout="centered"
)

# App Title
st.title("🌤️ Weather App")

# Input Box
city = st.text_input("Enter City Name")

# Search Button
if st.button("Search"):
    if not city:
        st.warning("Please enter a city name")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        # Extract data
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description'].title()
        icon = data['weather'][0]['icon']
        country = data['sys']['country']
        feels_like = data['main']['feels_like']

        sunrise = datetime.fromtimestamp(
            data['sys']['sunrise']
        )

        sunset = datetime.fromtimestamp(
            data['sys']['sunset']
        )

        # Success Message
        st.success("Weather Retrieved Successfully")

        # Location
        st.subheader(f"📍 {city.title()}, {country}")

        # Weather Icon
        st.image(
            f"https://openweathermap.org/img/wn/{icon}@2x.png",
            width=100
        )

        # Main Metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🌡️ Temperature",
                f"{temperature:.1f} °C"
            )

        with col2:
            st.metric(
                "💧 Humidity",
                f"{humidity}%"
            )

        with col3:
            st.metric(
                "🌬️ Wind",
                f"{wind_speed} m/s"
            )

        # Additional Metrics
        col4, col5 = st.columns(2)

        with col4:
            st.metric(
                "🤒 Feels Like",
                f"{feels_like:.1f} °C"
            )

        with col5:
            st.metric(
                "☁️ Weather",
                description
            )

        # Sunrise & Sunset
        st.subheader("🌅 Sun Information")

        col6, col7 = st.columns(2)

        with col6:
            st.metric(
                "Sunrise",
                sunrise.strftime("%H:%M")
            )

        with col7:
            st.metric(
                "Sunset",
                sunset.strftime("%H:%M")
            )

    else:
        st.error("❌ City not found or API key is invalid")
