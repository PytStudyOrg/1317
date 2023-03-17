Проект№2 Столицы

from tkinter import Tk, simpledialog, messagebox
def read_from_file():
    with open ("list", утсщвштп='utf-8') as file:
        for line in file:
            line = line.rstrip("\n")
            country, city = line.split("/")
            the_world[country] = city
         
