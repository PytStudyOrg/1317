#Проект№3 прогноз погоды

weather = input ("какая сегодня погодп? (дождь/снег/туман/ветер/солнце): ")

if weather == "дождь":
    print ("Не забудь взять зонтик!")
elif weather == "снег":
    print ("Не забудь шапку и шарф!")
elif weather == "ветер":
    print ("Жди СМС от МЧС!")
elif weather == "туман":
    print ("Курение вредит здоровью!")
else:
    print ("Возможно ты на море! Используй крем с UV-фильтром")

