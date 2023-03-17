#Проект№2 Столицы

from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open ("capital_data.txt", encoding='utf-8') as file:
        for line in file:
            line = line.rstrip("\n")
            country, city = line.split("/")
            the_world[country] = city

print ("Словарь столиц")
root = Tk()
root.withdraw()
the_world{}
         
der read_from_file():

while True:
    query_country = simpledialog.askstring("Страна", "Введите название страны")
    if query_country in the_world:
        rusult = the_world[query_country]
        messagebox.showinfo("Ответ", query_country + " : столица этой страны - " + result + " ! ")
    else:
        print ("Нет такой страны!")

