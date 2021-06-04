from Wallpaper import main

try:
    with open('user.txt', 'r') as file:
        city = file.read()
        print(f'If you want, you can change your city, just type chg \n'
              f'If you dont want, type start to start')
        w = input()

        if w == 'start':
            main(city)
        elif w == 'chg':
            city = input('Please, enter your city \n')
            with open('user.txt', 'w') as file:
                file.write(city)

            w = input('Start? \n')
            if w.lower() == 'start':
                main(city)
        else:
            print('command not found')


except FileNotFoundError:
    city = input('Please, enter your city \n')
    save = input('Should I save it (Y/N) \n')
    if save == 'Y':
        with open('user.txt', 'w') as file:
            file.write('city')
