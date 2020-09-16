from datetime import datetime

import file_functions
import weather_functions
import test_functions
from class_test import Product

dotest = False
#dotest = True
dofilestuff = False
#dofilestuff = True
doweather = False
doweather = True

product = Product("Drill", 40.99)
print(product.name + " " + str(product.price))

#testing stuff
if dotest:
    test_functions.test_string_printing()
    test_functions.some_maths()
    test_functions.loop_in_range()
    #test_functions.run()

#testing file reading writing
if dofilestuff:
    file_functions.file_write_api_key()
    file_functions.file_read_api_key()

#testing weather api
if doweather:
    api_key = file_functions.file_read_api_key()
    sampledata = weather_functions.get_weather("cardiff",api_key)
    print("Sample data:")
    print(str(sampledata))
    test_functions.time_delta()

    city_names = ["Cardiff","long%20ditton"]
    for city in city_names:
        data = weather_functions.get_weather(city,api_key)
        #print("got data: " + str(data))
        weather_functions.print_readable_data(weather_functions.load_json(data))
        print("\n")

    city_name = ''
    while city_name != 'quit' and (city_name != 'q'):
        city_name = input("enter city name:\n")
        if (city_name != 'quit') and (city_name != 'q'):
            data = weather_functions.get_weather(city_name,api_key)
            #print("got data: " + str(data))
            weather_functions.print_readable_data(weather_functions.load_json(data))

########

