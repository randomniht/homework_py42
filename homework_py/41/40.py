import random
class Car:
    def __init__(self, color_car, fuel_amount, fuel_consumption):
        self.color_car = color_car
        self.fuel_amount = fuel_amount
        self.fuel_consumption = fuel_consumption
        self.mileage = 0

    def drive(self, distance):

        required_fuel = (distance / 100) * self.fuel_consumption

        if required_fuel <= self.fuel_amount:
            self.fuel_amount -= required_fuel
            self.mileage += distance
            file_new = CheckFile()
            file_new.write(required_fuel, distance)
            print(f"Мы проехали {distance} км.")
        else:
            print("Не хватает топлива.")

    def get_mileage(self):
        print(f'Пробег / mileage - {self.mileage}, Осталось - {self.fuel_amount}')
    def print_color(self,color):
        _list_ = ['Желтый','Красный','Черный']
        if color in _list_:
            self.color_car = color
            print(f'Новый цвет {color}')
        else:
            print('no paint')
class CheckFile:
    def write(self, required_fuel, distance):
        with open('log.txt', 'a', encoding='utf-8') as f:
            a = f'required_fuel - {required_fuel}, distance - {distance} \n'
            f.write(a)
class SportCar(Car):
    def fast_drive(self,distance):
        required_fuel = ((distance / 100) * self.fuel_consumption) * 1.5

        if required_fuel <= self.fuel_amount:
            self.fuel_amount -= required_fuel
            self.mileage += distance
            file_new = CheckFile()
            file_new.write(required_fuel, distance)
            print(f"Мы проехали {distance} км.")
        else:
            print("Не хватает топлива.")
    def competition(self):
        a = random.randint(0,1)
        if a ==  0:
            print('lose')
        else:
            print('win')




        

car = Car(color_car="Красный", fuel_amount=100, fuel_consumption=100)
car.drive(50)
car.get_mileage()
car.drive(30)
car.get_mileage()
car.drive(10)
car.get_mileage()
car.print_color('Зеленый')
car.print_color('Черный')
car1 = Car(color_car='черный', fuel_amount=8, fuel_consumption=8)
car2 = SportCar(color_car='черный', fuel_amount=8,fuel_consumption=8)
print('Первая машина')
for i in range(4):
        car1.drive(30)
print('Вторая машина')
for i in range(4):
    car2.fast_drive(30)
car2.competition()

print('test')