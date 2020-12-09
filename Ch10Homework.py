# Chapter 10 Homework
# Jeffrey Nicholls (A00230615)
# December 8th, 2020
# Purpose: Create a program that uses a custom Car object, 
# calls the accelerate method five times and displays the speed 
# and distant. then calls the break method.
# Acknowledgments: none at time of writing


# Main Method

    # Menu to start program, 
    # Give user option to create or drive car
    # create car creates an instance of Car
    # drive car bring to sub menu to drive
    # drive menu is to use methods
    # get_speed after every method call

import car_class as cc 

def main():
    main_menu = True

    while main_menu:
        print("Welcome to the text car!")
        print("========================")
        print("1) Create New Car")
        print("2) Drive Car")
        print("3) Exit")
        user_input = input("Please enter a selection\n")

        if user_input == "1":
            year = input("What year model will the car be?\n")
            brand = input("What make will the car be?\n")
            car1 = cc.Car(year, brand)

        elif user_input == "2":
            try:
                # checking if car exists
                car1.accelerate()
                car1.brake()
                boolean = True

                while boolean:
                    print("       Car Menu")
                    print("========================\n")
                    print("You're currently travelling", 
                        car1.get_speed(), "km/h\n")
                    print("1) Accelerate")
                    print("2) Brake")
                    print("3) Return to main menu")
                    car_input = input("Enter Selection\n")
                    if car_input == "1":
                        car1.accelerate()
                    elif car_input == "2":
                        car1.brake()
                    elif car_input == "3":
                        boolean = False
                    else:
                        print("Invalid Selection")
            except Exception:
                print("There's no car yet")
                print("Please make one!")
        
        elif user_input == "3":
            main_menu = False
            print("Goodbye!")
        
        else:
            print("Invalid Selection")

main()

        


    

    