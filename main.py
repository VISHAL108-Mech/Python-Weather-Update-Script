"""Weather Alert App: Sends weather alerts via email"""
import requests
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

# Constants
WEATHER_KEY= os.environ.get("OWM_WEATHER_API_KEY")
MY_LAT= os.environ.get("ZNA_LAT")
MY_LONG= os.environ.get("ZNA_LONG")
USER_ID = os.environ.get("SMTP_GMAIL_ID")
ID_PASSWORD = os.environ.get("SMTP_GMAIL_PASSWORD")
API_END_POINT = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": WEATHER_KEY,
}

response = requests.get(API_END_POINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

today_weather = weather_data["weather"][0]["main"]

MESSAGE = f"Subject: Weather Alert!\n\n{today_weather} today."

# Send email alert
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=USER_ID, password=ID_PASSWORD)
    connection.sendmail(
        from_addr=USER_ID,
        to_addrs=USER_ID,
        msg=MESSAGE.encode("utf-8"),
    )
    print("Alert sent successfully.")
