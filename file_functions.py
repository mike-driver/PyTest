def file_write_api_key():
    file1 = open("app_config.txt", "w")  # append mode
    file1.write("now hidden .. just for initial file write\n")
    file1.close()

def file_read_api_key():
    file1 = open("c:/keys/weatherapikey/app_config.txt", "r")
    data = file1.readline()
    print ('api key:')
    print (data)
    return data