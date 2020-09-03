# comments

# by city id..
# weburl = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?id=2643743&APPID={api_key}")

# investigate:
# assert isinstance(data, object)
import json
from decimal import Decimal

def load_json(data):
    pyobject = json.loads(data)
    return pyobject

def print_readable_data(json_dict):
    kelvin_temp = json_dict['main']['temp']
    celsius_temp = round(Decimal(kelvin_temp - 273.15), 1)

    feels_like_kelvin_temp = json_dict['main']['feels_like']
    feels_like_celsius_temp = round(Decimal(feels_like_kelvin_temp - 273.15), 1)

    weather_description = json_dict['weather'][0]['main'] + ", " + json_dict['weather'][0]['description']
    location = str(json_dict['name']).upper()
    print(f"weather description in {location}: " + weather_description)
    print("temp: " + str(celsius_temp))
    print("feels like temp: " + str(feels_like_celsius_temp))
    #print("Sunrise: " + str(json_dict['sys']['sunrise']))


def get_weather(location, api_key):
    import urllib.request
    weburl = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}")
    #print("result code: " + str(weburl.getcode()))
    data = weburl.read()
    return data


def test_string_printing():
    print("printing strings".upper())
    print("Hello world")
    text1 = "Home Log Cabin"
    print(text1[:])
    print(text1[0:3])
    print(text1[-1:])

def some_maths():
    print("some maths".upper())
    int1 = 3
    float1 = 1.414
    is_true = True
    print(int1)
    print(float1)
    print(is_true)
    print(type(is_true))
