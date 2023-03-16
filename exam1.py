#Проект№1 генератор паролей
import random
import string
adjectives = ["сонный", "free" , "сонный" , "красный" , "большой" , "маленький" , "зеленый" , "смелый" , "ревнивый" , "горячий" , "крепкий" , "розовый" , "пушистый" , "яркий" , "черный" , "оригинальный" , "популярный" , "богатый" , "блестящий" , "синий"]
noun = ["яблоко" , "персик" ,"грушка" , "стол" , "круг" , "ручка" , "карандаш" , "панда" , "ластик" , "стол" , "стул" , "слон" , "цветок" , "лилия" , "мышь"]
print ("Добро пожаловать в генератор паролей!")
while True:
    adjectives = random.choice(adjectives)
    noun = random.choice(noun)    
    number = random.randrange(0, 1000)
    special_char = random.choice(string.punctuation)
    password = adjectives + noun + str(number) + special_char
    print ("новый пароль: %s" % password)
    response = input ("сгенерировать другой пароль? введите да или нет: ")
    if response == "нет":
        break