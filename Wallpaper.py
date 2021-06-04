import ctypes
import json
import time
import requests
from api_key_file import api_key_f


def get_weather(location_key):
    api_key = api_key_f
    req2 = requests.get(
        f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}').json()
    return req2[0]["WeatherText"]


def main(city):
    api_key = api_key_f
    req = requests.get(
        f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city}').json()
    location_key = req[0]["Key"]
    req2 = requests.get(
        f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}').json()
    if req2:
        print(f'Weather right now: {req2[0]["WeatherText"]}')
        main2(location_key)
    else:
        print('Network Error...')


def main2(location_key):
    print('Here you can freely create your wallpaper based on weather outside c: \n')
    try:
        with open('data.txt', 'r') as file:
            data = file.read()
        print('If you want, you can add more wallpapers, just type "add"')
        print('Or print "start" to launch the program')

    except FileNotFoundError:
        with open('data.txt', 'w') as file:
            pass
        print('To start, you have to create your wallpapers \n')
        print(f'How to do that: \n'
              f'1. Type "add" \n'
              f'2. Type what weather this wallpaper will appear with \n'
              f'3. Paste absolute path to this wallpaper \n'
              f'4. Profit :3')

    w = input()
    if w == 'add':
        d = dict()
        w = input('Type what weather this wallpaper will appear with \n')
        print('Paste absolute path to this wallpaper \n')
        w2 = input()
        d[w] = w2
        with open('data.txt', 'w') as file:
            json.dump(d, file)

    elif w == 'start':
        print('Type "stop" anytime you want to stop the program')
        with open('data.txt', 'r') as file:
            data = json.load(file)
        while True:
            try:
                path = data[get_weather(location_key)]
                print(path)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
            except KeyError:
                pass
            time.sleep(800)

