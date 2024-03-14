# Author: Peyton J. Hall (C)
"""
This Python program converts a Degree Minute Second (DMS) measurement
to Radian measurement. Radians are preferred over degrees in
Calculus because they simplify trigonometric functions and their 
calculations. Latitude and longitude can be expressed in radians
as well, so this program's usage is versatile.
"""

import math
from fractions import Fraction

def DMS_to_Radians(d, m, s):
    # Convert DMS to decimal degrees
    decimal_degrees = d + m / 60 + s / 3600
    # Convert decimal degrees to radians
    radians = decimal_degrees * math.pi / 180
    return radians

def Validate_Input(prompt, valid_values, max_value = None, error_message = None): # default parameters
    value = None
    while value is None:
        try:
            value = input(prompt).upper()
            if value not in valid_values:
                if error_message is not None:
                    print(error_message)
                else:
                    print(f"Invalid input. Please enter {', '.join(valid_values[:-1])} or {valid_values[-1]}.")
                value = None
            elif max_value is not None and value.isdigit() and int(value) > max_value:
                print("Invalid input. Please enter a valid value.")
                value = None
        except ValueError: # built-in exception
            print("Invalid input. Please enter a valid value.")
    return value

def Simplify_Fraction(radians):
    # use .limit_denominator() from fractions module to simplify a fraction
    simplified = Fraction(radians / math.pi).limit_denominator()
    if simplified.denominator == 1: # .denominator attribute built-in by module
        return f"{simplified.numerator}π" # .numerator attribute built-in, also
    else:
        return f"{simplified.numerator}π/{simplified.denominator}"

def Convert_Measurement():
    print("Convert Degree Minute Second (DMS) coordinates to to Radians.\n")

    # Prompt the user for latitude DMS coordinates
    latitude_degrees = int(Validate_Input("Enter latitude degrees° (0 to 90): ", [str(i) for i in range(91)]))
    latitude_minutes = int(Validate_Input("Enter latitude minutes' (0 to 59): ", [str(i) for i in range(60)]))
    latitude_seconds = int(Validate_Input("Enter latitude seconds\" (0 to 59): ", [str(i) for i in range(60)]))

    # Prompt the user for latitude hemisphere (N/S)
    latitude_hemisphere = Validate_Input("Enter latitude hemisphere (N or S): ", ['N', 'S'], 
                                         error_message = "Invalid input. Please enter \"N\" or \"S\"")

    # Prompt the user for longitude DMS coordinates
    longitude_degrees = int(Validate_Input("Enter longitude degrees° (0 to 180): ", [str(i) for i in range(181)]))
    longitude_minutes = int(Validate_Input("Enter longitude minutes' (0 to 59): ", [str(i) for i in range(60)]))
    longitude_seconds = int(Validate_Input("Enter longitude seconds\" (0 to 59): ", [str(i) for i in range(60)]))

    # Prompt the user for longitude hemisphere (E/W)
    longitude_hemisphere = Validate_Input("Enter longitude hemisphere (E or W): ", ['E', 'W'], 
                                          error_message = "Invalid input. Please enter \"E\" or \"W\"")

    # Convert latitude and longitude DMS coordinates to radians
    latitude_radians = DMS_to_Radians(latitude_degrees, latitude_minutes, latitude_seconds)
    longitude_radians = DMS_to_Radians(longitude_degrees, longitude_minutes, longitude_seconds)

    # Simplify radians into a more readable form
    simplified_latitude = Simplify_Fraction(latitude_radians)
    simplified_longitude = Simplify_Fraction(longitude_radians)

    print(f"Latitude in radians: {latitude_radians} or {simplified_latitude}")
    print(f"Longitude in radians: {longitude_radians} or {simplified_longitude}")

    
if __name__ == "__main__":
    Convert_Measurement() # call the main method

"""
Unit Circle:
Radius = 1
π = circumference / diameter = 180°
2π = one whole unit circle = 360°
"""