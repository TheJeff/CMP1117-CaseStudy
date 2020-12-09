# Chapter 10 Homework
# Jeffrey Nicholls (A00230615)
# December 8th, 2020
# Purpose: Create a program that uses a custom Car object, 
# calls the accelerate method five times and displays the speed 
# and distant. then calls the break method.
# Acknowledgments: none at time of writing

# Car Object

    # Attributes:
        # year_model: the year model (string)
        # make: Manufacturer (String)
        # speed: Cars speed (int or float)

    # Methods:
        # Accelerate: add 5 to speed
        # Brake: subtract 5 from speed
        # get_speed: return current speed variable
        
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def brake(self):
        self.__speed -= 5
        if self.__speed <= 0:
            print("Car has stopped\n")
            self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def get_speed(self):
        return self.__speed