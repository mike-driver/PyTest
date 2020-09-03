# comments

# by city id..
# weburl = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?id=2643743&APPID={api_key}")

# investigate:
# assert isinstance(data, object)
import json


def load_json(data):
    #print (data)
    pyobject = json.loads(data)
    #print (pyobject['main'])
    #value = input("wait for input.....")
    return pyobject

def get_weather(location, api_key):
    import urllib.request
    weburl = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}")
    print("result code: " + str(weburl.getcode()))
    data = weburl.read()
    return data

def file_write_api_key():
    file1 = open("app_config.txt", "w")  # append mode
    file1.write("now hidden .. just for initial file write\n")
    file1.close()

def file_read_api_key():
    #file1 = open("app_config.txt", "r")
    file1 = open("c:/users/mdriver/weatherapikey/app_config.txt", "r")
    data = file1.readline()
    print ('api key:')
    print (data)
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
