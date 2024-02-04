import requests
from twilio.rest import Client


ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
appid = "da4dcaf9cc9e54cbb230f2549ecd0443"
lat = "48.552750909204676"
lon = "22.07290649414063"

#twillio account
account_sid = 'ACccf6a0b5996fa291f0fb55826f4b7c23'
auth_token = 'bf592bea4267f6fe5c6fc952fe4e7647'


weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": appid,
    "cnt": 4,
}

response = requests.get(ENDPOINT, params=weather_params)
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+18126184552',
        body ='Ma esni fog.',
        to='+421948219530'
    )


