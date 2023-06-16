class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        print("Транспорт движется")

class Car(Vehicle):
    def drive(self):
        print(f"Автомобиль {self.brand} едет по дороге")

class Bicycle(Vehicle):
    def drive(self):
        print(f"Велосипед {self.brand} катится по тротуару")

class Motorcycle(Vehicle):
    def drive(self):
        print(f"Мотоцикл {self.brand} мчится по шоссе")

car = Car("BMW")
bicycle = Bicycle("Trek")
motorcycle = Motorcycle("Honda")

car.drive()
bicycle.drive()
motorcycle.drive()
