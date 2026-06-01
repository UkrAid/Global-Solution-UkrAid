"""
My support functions
"""

import os

def println(str_):
    print(str_, "\n")

def separador():
    print("═" * 55 + "\n")

def separador_up():
    print("╔" + "═" * 53  + "╗" + "\n")

def separador_down():
    print("╚" + "═" * 53 + "╝" + "\n")

def pause():
    input("Press enter to return...\n")

def clear():
    os.system("cls" if os.name == "nt" else "clear")