import pyshorteners
from colorama import Fore, init
init()
url = input("Introduzca una URL: ")
s = pyshorteners.Shortener().tinyurl.short(url)
print(Fore.GREEN + "Tu URL acortada es", s)