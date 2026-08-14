class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    def drive(self):
        print("Driving the car")
    def show_info(self):
        print(f"The car name is {self.name} and brand is {self.brand}")
class Battery:
    def charge(self):
        print("the battery is charging")
    def check_range(self):
        current_charge = int(input("Please enter current charge: "))
        Range = current_charge * 4
        print(f"The remaining estimated range is: {Range} Km")
class ElectricCar(Car, Battery):
    def __init__(self, name, brand):
       super().__init__(name, brand)
electric_car = ElectricCar("Model 3", "Tesla")
electric_car.drive()
electric_car.show_info()
electric_car.charge()
electric_car.check_range()
