class Automobile:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # Ниже методы являются методами-модицикаторами атрибутов данных класса Automobile
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # Ниже методы являются методами-получателями атрибутов данных класса Automobile
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

# Создаем класс Car - легковой автомобиль. Он является подклассом класса Automobile
class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):        # Метод __init__ принимает аргументы для фирмы-изготовителя, модели, пробега, цены и количества дверей
        Automobile.__init__(self, make, model, mileage, price)     # Вызываем метод __init__ надкласса и передаем требуемые аргументы классу Car
        self.__doors = doors                                       # Инициализируем атрибут __doors

    def set_doors(self, doors):
        self.__doors = doors

    def get_doors(self):
        return self.__doors

# Создаем класс Truck - пикап.
class Truck(Automobile):
    def __init__(self, make, model, mileage, price, drive_type):
        Automobile.__init__(self, make, model, mileage, price)
        self.__drive_type = drive_type

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    def get_drive_type(self):
        return self.__drive_type

# Создаем класс SUV - джип.
class SUV(Automobile):
    def __init__(self, make, model, mileage, price, pass_cap):
        Automobile.__init__(self, make, model, mileage, price)
        self.__pass_cap = pass_cap

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    def get_pass_cap(self):
        return self.__pass_cap
