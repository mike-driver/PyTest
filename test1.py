import file_functions
import functions
from decimal import Decimal

api_key = file_functions.file_read_api_key()
sampledata = functions.get_weather("cardiff",api_key)
print("Sample data:")
print(str(sampledata))
print("")

city_names = ["london","Cardiff","edinburgh","leeds","plymouth","toronto","denver","Longyearbyen","Ushuaia","Kirkwall","Windy%20City"]
for city in city_names:
    data = functions.get_weather(city,api_key)
    functions.print_readable_data(functions.load_json(data))
    print("")

city_name = ''
while city_name != 'quit':
    city_name = input("enter city name:\n")
    if city_name != 'quit':
        data = functions.get_weather(city_name,api_key)
        functions.print_readable_data(functions.load_json(data))


