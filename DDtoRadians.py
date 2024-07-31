# Author: Peyton J. Hall (C)
"""
This Python program converts a Decimal Degree (DD) measurement
to Radian measurement. Radians are preferred over degrees in
Calculus because they simplify trigonometric functions and their 
calculations for mathematicians. Latitude and longitude can be 
expressed in radians as well, so this program's usage is versatile.
"""

import math
from fractions import Fraction

def DD_to_Radians(dd):
    # Use the conversion formula for degrees to radians
    radians = dd * math.pi / 180
    return radians

def Validate_Input():
    while True:
        try:
            dd = float(input("Enter decimal degrees: "))
            return dd
        except ValueError as e:
            print("Invalid input:", e)

def Simplify_Fraction(radians):
    # use .limit_denominator() from fractions module to simplify a fraction
    simplified = Fraction(radians / math.pi).limit_denominator()
    if simplified.denominator == 1: # .denominator attribute built-in by module
        return f"{simplified.numerator}π" # .numerator attribute built-in, also
    else:
        return f"{simplified.numerator}π/{simplified.denominator}"

def Convert_Measurement():
    print("Convert Decimal Degrees to Radians.\n")
    dd = Validate_Input()
    radians = DD_to_Radians(dd)
    simplified_fraction = Simplify_Fraction(radians)
    print(f"{dd}° is equivalent to {simplified_fraction}")

if __name__ == "__main__":
    Convert_Measurement() # call the main method

"""
Unit Circle:
Radius = 1
π = circumference / diameter = 180°
2π = one whole unit circle = 360°
"""
