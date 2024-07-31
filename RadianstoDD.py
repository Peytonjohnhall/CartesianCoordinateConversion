# Author: Peyton J. Hall (C)
"""
This Python program converts a Radian measurement to 
Decimal Degree (DD) measurement. Radians are preferred over degrees in
Calculus because they simplify trigonometric functions and their 
calculations for mathematicians. Latitude and longitude can be 
expressed in radians as well, so this program's usage is versatile.
"""

import math

def Radians_to_DD(numerator, denominator):
    # Use the conversion formula for radians to decimal degree
    radians = (numerator * math.pi) / denominator
    decimal_degrees = radians * (180 / math.pi)
    return decimal_degrees

def Validate_Input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError as e:
            print("Invalid input:", e)

def Convert_Measurement():
    print("Convert Radians to Decimal Degrees.\n")

    numerator = Validate_Input("Enter the numerator of the radians fraction: ")
    denominator = Validate_Input("Enter the denominator of the radians fraction: ")

    decimal_degrees = Radians_to_DD(numerator, denominator)
    print(f"The value in decimal degrees is: {decimal_degrees}")

if __name__ == "__main__":
    Convert_Measurement() # call the main method

"""
Unit Circle:
Radius = 1
π = circumference / diameter = 180°
2π = one whole unit circle = 360°
"""
