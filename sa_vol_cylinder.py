#!/usr/bin/env python3
# Created by: Layla Michel
# Created on: Apr. 29, 2021
# This program calculates the surface area and volume of a cylinder.

import math


def main():
    # Welcome message
    print("Hello, today we will calculate the surface\
 area and volume of a cylinder using numbers you input!")
    radius_value()


def radius_value():
    # Ask the user to input a valid value for the radius
    global radius

    # Checks for errors in the input
    # This code was taken and modified from
    # https://pynative.com/python-check-user-input-is-number-or-string/
    try:
        radius = float(input("To start off type\
 in the radius of the cylinder (cm): "))
        if (radius < 0):
            # Error message for if it's a negative number
            print("The value must be a positive number")
            radius_value()
        else:
            height_value()
    except ValueError:
        # Error message for if it's a letter/string
        print("The value you entered was not a valid number.")
        radius_value()


def height_value():
    # Ask the user to input a valid value for the height
    global height

    # Checks for errors in the input
    # This code was taken and modified from
    # https://pynative.com/python-check-user-input-is-number-or-string/
    try:
        height = float(input("And now its height (cm): "))
        if (height < 0):
            # Error message for if it's a negative number
            print("The value must be a positive number")
            height_value()
        else:
            calc_sa_vol()
    except ValueError:
        # Error message for if it's a letter/string
        print("The value you entered was not a valid number.")
        height_value()


def calc_sa_vol():
    # Calculate and display the area and perimeter, rounding it to 2 decimals
    print("\n")
    print("With those values,")
    print("The surface area will be: {:.2f} cm^2\
". format(2*math.pi*radius*height+2*math.pi*radius**2))
    print("And the volume will be: {:.2f}\
 cm^3 ". format(radius**2*math.pi*height))


if __name__ == "__main__":
    main()
