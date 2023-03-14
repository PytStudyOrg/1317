# вывести все простые числа в диапазоне от 2 до 100

for number in range(2, 25):
    if number > 1:
        for i in range(2, number):
            if(number % i) == 0:
                break
            else:
                print(number)