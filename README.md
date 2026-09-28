# 🌦️ Weather Update App

A Python automation that checks the current weather for your exact location and emails you an update — so you know whether to grab an umbrella or sunglasses before you even step outside.

> Run it each morning and get today's weather condition delivered straight to your inbox, no app-checking required.

---

## 🎮 Demo

<img width="380" height="175" alt="Screenshot 2026-09-28 103417" src="https://github.com/user-attachments/assets/222341e0-08c5-4ef0-8846-23f408ad8ef1" />

---

## ✨ Features

- 🌍 **Location-based weather lookup** — pulls live conditions for your latitude/longitude from the OpenWeatherMap API.
- ✉️ **Automatic email delivery** through Gmail's SMTP server with a secure TLS connection.
- 🔒 **Secure configuration** — API keys, Gmail credentials, and coordinates are all loaded from environment variables via `python-dotenv`, never hardcoded.
- 🛡️ **Fail-loud API handling** — `raise_for_status()` makes sure a failed API request stops the script instead of silently sending a bad email.
- 🕒 **Schedule-friendly design** — a single-run script that fits naturally into cron, Task Scheduler, GitHub Actions, or PythonAnywhere.

---

## 🛠️ Tech Stack

| Category | Tool / Concept |
|---|---|
| Language | Python 3 |
| API | [OpenWeatherMap Current Weather API](https://openweathermap.org/current) |
| HTTP Requests | `requests` |
| Email | `smtplib` (standard library) — SMTP + TLS email delivery |
| Secrets Management | `python-dotenv` |
| Core Concepts | REST API integration, JSON parsing, environment variables, email automation |

---

## 📂 Project Structure

```
Weather Update App/
│
├── main.py     # Entry point — fetches weather data and sends the email
├── .env         # Your API key, Gmail credentials, and coordinates (never committed)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- A free [OpenWeatherMap API key](https://openweathermap.org/api)
- `requests` and `python-dotenv` — install via pip:

```bash
pip install requests python-dotenv
```

### Setup

**1. Create your `.env` file** in the project root:

```
OWM_WEATHER_API_KEY=your_openweathermap_api_key
ZNA_LAT=your_latitude
ZNA_LONG=your_longitude
SMTP_GMAIL_ID=your_email@gmail.com
SMTP_GMAIL_PASSWORD=your_app_password
```

> ⚠️ Use a [Gmail App Password](https://myaccount.google.com/apppasswords), not your real Gmail password — Google blocks plain-password SMTP logins by default. Add `.env` to your `.gitignore` so it never gets pushed to GitHub.

### Run it
```bash
python main.py
```

### Automate it
Schedule the script to run once a day with any of these:
- **Cron** (macOS/Linux): `0 7 * * * /usr/bin/python3 /path/to/main.py` — runs daily at 7 AM
- **Task Scheduler** (Windows): create a daily trigger pointing to the script
- **GitHub Actions**: use a [`schedule`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule) trigger to run it from GitHub's infrastructure
- **PythonAnywhere**: set up a free Scheduled Task to run it daily in the cloud

---

## 🧩 How It Works

### 1. Loading Configuration Securely
All secrets and personal details are pulled from environment variables, keeping them out of the source code.

```python
load_dotenv()

WEATHER_KEY= os.environ.get("OWM_WEATHER_API_KEY")
MY_LAT= os.environ.get("ZNA_LAT")
MY_LONG= os.environ.get("ZNA_LONG")
USER_ID = os.environ.get("SMTP_GMAIL_ID")
ID_PASSWORD = os.environ.get("SMTP_GMAIL_PASSWORD")
API_END_POINT = "https://api.openweathermap.org/data/2.5/weather"
```

### 2. Fetching Today's Weather
The script sends your coordinates and API key to OpenWeatherMap, then extracts the main weather condition (e.g. Clear, Clouds, Rain) from the JSON response.

```python
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": WEATHER_KEY,
}

response = requests.get(API_END_POINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

today_weather = weather_data["weather"][0]["main"]
```

### 3. Sending the Email Update
The weather condition is dropped into a message and sent through Gmail's SMTP server over a secure TLS connection.

```python
MESSAGE = f"Subject: Weather Update!\n\n{today_weather} today."

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=USER_ID, password=ID_PASSWORD)
    connection.sendmail(
        from_addr=USER_ID,
        to_addrs=USER_ID,
        msg=MESSAGE.encode("utf-8"),
    )
    print("Update sent successfully.")
```

---

## 📚 What This Project Demonstrates

- Consuming a third-party REST API with query parameters and API-key authentication
- Navigating nested JSON responses to extract the exact field needed
- Sending automated emails programmatically with `smtplib` and TLS
- Managing secrets and configuration with environment variables
- Building a script designed to run unattended on a schedule

---

## 🔮 Future Improvements

- [ ] Add an optional alert mode — only send an email when conditions are worth flagging (e.g. rain or snow), instead of on every run
- [ ] Use the forecast endpoint so the email covers the whole day, not just the current moment
- [ ] Include richer details in the message: temperature, city name, and humidity
- [ ] Convert temperature units (the API returns Kelvin by default unless `units` is specified)
- [ ] Add logging and a dry-run mode for safe testing

---

## 👤 Developer

**VISHAL YADAV**
- GitHub: [@VISHAL108-Mech](https://github.com/VISHAL108-Mech)
- LinkedIn: [vishal-yadav-2a91a7428](https://www.linkedin.com/in/vishal-yadav-2a91a7428)
- Email: [vy4122000@gmail.com](mailto:vy4122000@gmail.com)
