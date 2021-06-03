import ctypes
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(20, 0, "E:\Testfolder\Jpic.png" , 0)