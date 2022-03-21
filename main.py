import requests
import os
from twilio.rest import Client

account_sid = ''
auth_token = ""

api_key = ""
parameters = {
    "lat": 36.375431,
    "lon": 140.461044,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    hour_data["weather"]
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today! Bring an ☂.",
        from_='+15043863670',
        to="+818012069191"
    )

    print(message.status)
