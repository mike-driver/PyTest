import functions

# functions.test_string_printing()
# functions.some_maths()
#functions.file_write_api_key()

api_key = functions.file_read_api_key()

data = functions.get_weather('frankfurt',api_key)
print ('FRANKFURT')
print(data)

json_stuff = functions.load_json(data)
print('json stuff: ')
print (json_stuff)
print ("Sunrise: " + str(json_stuff['sys']['sunrise']))
sunrise = json_stuff['sys']['sunrise'] / 86400 + 25569
print (sunrise)

city_names = ["london","new%20york","cairo","cardiff","paris","madrid", "bangkok","denver","LiverPOol"]
for city in city_names:
    data = functions.get_weather(city,api_key)
    print(city.capitalize())
    print(data)

city_name = ''
while city_name != 'quit':
    city_name = input("enter city name:\n")
    if city_name != 'quit':
        data = functions.get_weather(city_name,api_key)
        print(city_name.upper())
        print (data)



