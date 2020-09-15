from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler

def time_delta():
    # Using current time
    ini_time_for_now = datetime.now() + timedelta(days=2)
    # printing initial_date
    print("initial_date", str(ini_time_for_now))
    # Calculating future dates
    future_date_after_someseconds = ini_time_for_now + timedelta(seconds=3600)
    future_date_after_2days = ini_time_for_now + timedelta(days=2)
    # printing calculated future_dates
    print('future_date_after_somesecs:', str(future_date_after_someseconds))
    print('future_date_after_2days:', str(future_date_after_2days))


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

def loop_in_range():
    for x in range(0, 3):
        print("X is equal to %d" % (x))
        print(f"X is equal to {x}")
    print("\n")

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()