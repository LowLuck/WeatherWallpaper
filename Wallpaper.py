import ctypes
import json


def main2():
    SPI_SETDESKWALLPAPER = 20
    print('Here you can freely create your wallpaper based on weather outside c: \n')
    print('To start, you have to create your wallpapers \n')
    print(f'How to do that: \n'
          f'1. Type "add" \n'
          f'2. Type what weather this wallpaper will appear with \n'
          f'3. Paste absolute path to this wallpaper \n'
          f'4. Profit :3')
    try:
        with open('data.txt', 'r') as file:
            data = file.read()
    except FileNotFoundError:
        with open('data.txt', 'w') as file:
            pass

    w = input()
    if w == 'add':
        d = dict()
        w = input('Type what weather this wallpaper will appear with \n')
        print('Paste absolute path to this wallpaper \n')
        w2 = input()
        d[w] = w2
        with open('data.txt', 'w') as file:
            json.dump(d, file)
# ctypes.windll.user32.SystemParametersInfoW(20, 0, "E:\Testfolder\Jpic.png", 0)
