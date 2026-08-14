class Garage:

def __init__(self):  
    self.__capacity = 6  
    self.__total_cars = []  
    self.__parked_cars = []  
    self.__available_spots = self.__capacity  
def add_car(self,brand):  
    if brand not in self.__total_cars :  
        self.__total_cars.append(brand)  
def park_car(self,brand):  
    if self.__available_spots == 0:  
        return 0  
    if brand not in self.__parked_cars and brand in self.__total_cars:  
        self.__parked_cars.append(brand)  
        self.__available_spots = self.__available_spots - 1  
def remove_car(self,brand):  
    if brand in self.__parked_cars:  
        self.__parked_cars.remove(brand)  
        self.__total_cars.remove(brand)  
        self.__available_spots = self.__available_spots + 1  
def display_available_spots(self):  
    print(f"Number of available spots is: {self.__available_spots}")

