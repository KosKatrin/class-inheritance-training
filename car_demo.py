# Демонстрирует класс Car
# Импортируем модуль vehicles, который содержит определения классов Automobile и Car
import vehicles

def main():
    # Создаем экземпляр класса(объект класса) на основе класса Car
    # Легковое авто: 2001 BMW с 70 000 миль пробега, ценой $15 000 и с 4 дверьми
    car = vehicles.Car('BMV', 2001, 70000, 15000, 4)

    # Создаем экземпляр класса на основе класса Truck
    # Пикап: 2002 год, Toyota с 40000 милями пробега, ценой $12 000 и с 4-колесным приводом
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000, '4WD')

    # Создаем экземпляр класса на основе класса SUV
    # Джип: 2000 год, Volvo с 30 000 милями пробега, ценой $18 500 и вместимостью 5 человек
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500, 5)

    print('ПОДЕРЖАННЫЕ АВТО НА СКЛАДЕ')
    print('==========================')

    # Выводим данные легкового авто
    print('Данный легковой автомобиль имеется на складе:')
    print('Изготовитель:', car.get_make())
    print('Модель:', car.get_model())
    print('Пробег:', car.get_mileage())
    print('Цена:', car.get_price())
    print('Количество дверей:', car.get_doors())
    print()

    # Выводим данные пикапа
    print('Данный пикап имеется на складе:')
    print('Изготовитель:', truck.get_make())
    print('Модель:', truck.get_model())
    print('Пробег:', truck.get_mileage())
    print('Цена:', truck.get_price())
    print('Тип привода:', truck.get_drive_type())
    print()

    # Выводим данные джипа
    print('Данный джип имеется на складе:')
    print('Изготовитель', suv.get_make())
    print('Модель:', suv.get_model())
    print('Пробег:', suv.get_mileage())
    print('Цена:', suv.get_price())
    print('Пассажирская вместимость:', suv.get_pass_cap())
    print()

# вызываем главную функцию
main()

