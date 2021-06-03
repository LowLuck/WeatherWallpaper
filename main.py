# api key
# p6gwoTEl8qSHNP9EFSj9fW8YRNvn0wA9

# how to
# https://developer.accuweather.com/accuweather-locations-api/apis/get/locations/v1/cities/search
# https://developer.accuweather.com/accuweather-current-conditions-api/apis/get/currentconditions/v1/%7BlocationKey%7D

# premade requests
# http://dataservice.accuweather.com/locations/v1/cities/search?apikey=p6gwoTEl8qSHNP9EFSj9fW8YRNvn0wA9&q=Tver
# http://dataservice.accuweather.com/currentconditions/v1/296079?apikey=p6gwoTEl8qSHNP9EFSj9fW8YRNvn0wA9


import ctypes
import requests
SPI_SETDESKWALLPAPER = 20
# ctypes.windll.user32.SystemParametersInfoW(20, 0, "E:\Testfolder\Jpic.png" , 0)

try:
    with open('user.txt', 'r') as file:
        city = file.read()

except FileNotFoundError:
    city = input('Please, enter your city \n')
    save = input('Should I save it (Y/N) \n')
    if save == 'Y':
        with open('user.txt', 'w') as file:
            file.write('city')


api_key = 'p6gwoTEl8qSHNP9EFSj9fW8YRNvn0wA9'
req = requests.get(f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city}').json()
location_key = req[0]["Key"]
print(location_key)
req2 = requests.get(f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}').json()
if req2:
    print(req2[0]['WeatherText'])
else:
    print('err')