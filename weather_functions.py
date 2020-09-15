# comments

# by city id..
# weburl = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?id=2643743&APPID={api_key}")

# investigate:
# assert isinstance(data, object)
import json
from decimal import Decimal
import urllib.request
from urllib.error import HTTPError
from datetime import datetime, timedelta


def load_json(data):
    pyobject = json.loads(data)
    return pyobject


def print_readable_data(json_dict):
    longitude = str(json_dict['coord']['lon'])
    latitude = str(json_dict['coord']['lat'])
    kelvin_temp = json_dict['main']['temp']
    celsius_temp = round(Decimal(kelvin_temp - 273.15), 1)
    feels_like_kelvin_temp = json_dict['main']['feels_like']
    feels_like_celsius_temp = round(Decimal(feels_like_kelvin_temp - 273.15), 1)
    wind_strength = json_dict['wind']['speed']
    wind_direction = json_dict['wind']['deg']
    humidity = json_dict['main']['humidity']
    weather_description = json_dict['weather'][0]['main'] + ", " + json_dict['weather'][0]['description']
    location = str(json_dict['name']).upper()
    country = str(json_dict['sys']['country'])
    DST = 3600
    seconds_zone = json_dict['timezone'] - DST
    current_time = datetime.now().strftime("%H:%M:%S")
    sunriseunix = str(json_dict['sys']['sunrise']+seconds_zone)
    sunrise = datetime.fromtimestamp(int(sunriseunix)).strftime('%H:%M:%S')
    sunsetunix = str(json_dict['sys']['sunset']+seconds_zone)
    sunset = datetime.fromtimestamp(int(sunsetunix)).strftime('%H:%M:%S')

    print(f"Weather  for {location}, {country}, longitude {longitude}, latitude {latitude} on {datetime.now().date()} at {current_time} (BST) :")
    print(weather_description)
    print(f"Temp.: {celsius_temp} (C), Feels like : {feels_like_celsius_temp} (C)")
    print("Humidity: " + str(humidity))
    print("Wind strength: " + str(wind_strength) + ", " + "Wind direction: " + str(wind_direction))
    print("Sunrise: " + sunrise)
    print("Sunset: " + sunset)


def get_weather(location, api_key):
    try:
        weburl = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}")
        # print("result code: " + str(weburl.getcode()))
        data = weburl.read()
    except HTTPError as err:
        if err.code != 200:
            print("Error in City name!!!! .... but here's the weather in Cardif :-) ")
            return get_weather("cardiff", api_key)
            # exit(1)
            data = weburl.read()
    return data
