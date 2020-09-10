import file_functions
import weather_functions

from test_functions import loop_in_range
loop_in_range()

api_key = file_functions.file_read_api_key()
sampledata = weather_functions.get_weather("cardiff",api_key)
print("Sample data:")
print(str(sampledata))
print("\n")

city_names = ["london","Cardiff","edinburgh","leeds","plymouth","toronto","denver","Longyearbyen","Ushuaia","Kirkwall","Windy%20City","kansas","kansas%20city"]
for city in city_names:
    data = weather_functions.get_weather(city,api_key)
    weather_functions.print_readable_data(weather_functions.load_json(data))
    print("\n")

city_name = ''
while city_name != 'quit' and (city_name != 'q'):
    city_name = input("enter city name:\n")
    if (city_name != 'quit') and (city_name != 'q'):
        data = weather_functions.get_weather(city_name,api_key)
        weather_functions.print_readable_data(weather_functions.load_json(data))


