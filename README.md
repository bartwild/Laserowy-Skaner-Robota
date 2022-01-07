Wywołanie programu:
W terminalu wpisać: 
python3 Robot.py -h aby zobaczyc argumenty wywołania. Program ma domyślne argumenty, które są plikami zawartymi w poleceniu - wszystkie pliki wtedy należy zamieścić w tym samym folderze.
Mój program przyjmuje 3 pliki wejściowe. Obraz o wymiarach 320x240p (.png) z czarnymi kreskami na białym tle, plik tekstowy (.txt) w
postaci:

x = 130

y = 88

α = 226

oraz plik wczytujący konfigurację(.txt) tj. pożądane wymiary obrazu, ilość obrotów i kąt obrotu:

[DEFAULT]

image_width = 320

image_height = 240

rotation_angle = 10

total_angle = 180

pliki wyjściowe to plik tekstowy i obraz określone przez użytkownika.
