import requests
from Wallpaper import main2
from api_key_file import api_key_f


def main(city):
    api_key = api_key_f
    req = requests.get(
        f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city}').json()
    location_key = req[0]["Key"]
    req2 = requests.get(
        f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}').json()
    if req2:
        print(f'Weather right now:{req2[0]["WeatherText"]}')
        main2()
    else:
        print('Network Error...')
