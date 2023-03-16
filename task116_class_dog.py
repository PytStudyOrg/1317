class Dog():
    def __init__(self, name="", year=0) - > None:
        Dog.counter += 1
        self.id=Dog.counter
        self.name=name
        self.year=year
        print("Создан ",self.__str__())
    def __str__ (self):
        return "Собака:  " + self.name + " , " + str(self.year)