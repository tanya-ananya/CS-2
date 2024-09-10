'''
Author: Taaruni Ananya
'''

import math

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

class Car:
    def __init__(self, name, location, cost):
        self.name = name
        self.location = location
        self.cost = cost
    def __str__(self):
        return f'[{self.name}, {self.location}, {self.cost}]'
    def move_to(self, new_x, new_y):
        self.location.x = new_x
        self.location.y = new_y     
     
class Passenger:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def __str__(self):
        return f'[{self.name}, {self.location}]'
    def move_to(self, new_x, new_y):
        self.location.x = new_x
        self.location.y = new_y   
    
class RideSharingApp:
    def __init__(self):
        self.cars = []
        self.passengers = []
    def add_car(self, car):
        self.cars.append(car)

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def remove_car(self, car):
        self.cars.remove(car)

    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)

    def find_cheapest_car(self):
        cheapest_car = self.cars[0]
        cheapest_cost = cheapest_car.cost
        for car in self.cars:
            if car.cost < cheapest_cost:
                cheapest_car = car
                cheapest_cost = car.cost
        print(f'Cheapest car available: {cheapest_car.name}, Cost per mile: {cheapest_cost}')

    def find_nearest_car(self, passenger):
        best_car = self.cars[0]
        shortest_distance = 1000
        passenger_x = passenger.location.x
        passenger_y = passenger.location.y

        for car in self.cars:
            car_x = car.location.x
            car_y = car.location.y
            dist = math.sqrt((car_x - passenger_x) ** 2 + (car_y - passenger_y) ** 2)

            if dist < shortest_distance:
                best_car = car
                shortest_distance = dist

        print(f'Nearest car for {passenger.name}: {best_car.name}, Distance: {round(shortest_distance, 2)}')

#For the remaining code (after this line), no modification is required
print('---------------------Object creation------------------')
location1 = Location(2,1)
location2 = Location(-4,1)
car1 = Car('car1', location1, 0.61)
car2 = Car('car2', location2, 0.50)
print('Car object 1 created:',car1)
print('Car object 2 created:', car2)

location3 = Location(-2,3)
location4 = Location(0,0)
passenger1 = Passenger('passenger1', location3)
passenger2 = Passenger('passenger2', location4)
print('Passenger object 1 created:', passenger1)
print('Passenger object 2 created:', passenger2)

mobileApp = RideSharingApp()
mobileApp.add_car(car1)
mobileApp.add_car(car2)
mobileApp.add_passenger(passenger1)
mobileApp.add_passenger(passenger2)

print('-----------------------Scenario 1---------------------')
mobileApp.find_cheapest_car()
mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 2---------------------')
car1.move_to(0,-5)
passenger1.move_to(0,3)
print('car1\'s location has been updated:',car1)
print('passenger1\'s location has been updated:', passenger1)

mobileApp.find_cheapest_car()
mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 3---------------------')
car3= Car('car3', Location(0,2), 0.3)
mobileApp.add_car(car3)
print('New car added:',car3)
mobileApp.find_cheapest_car()
mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

