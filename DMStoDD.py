# Author: Peyton J. Hall (C)
"""
This Python program converts Degree Minute Second (DMS) 
coordinates to Decimal Degree (DD) coordinates, according 
to the WGS84 datum of the Cartesian coordinate system.
"""

# Conversion Formula for d°m's" to d.d° = d+(m/60)+(s/3600) = d.d°
def DMS_to_DD(d, m, s):
    # Implement conversion formula in function
    dd = d + (m / 60) + (s / 3600)
    return dd

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

# main method
def Convert_Coordinates():
    print("Convert Degree Minute Second (DMS) coordinates to Decimal Degree (DD) coordinates.\n")

    # Prompt the user for latitude DMS coordinates
    latitude_degrees = Validate_Input("Enter latitude degrees° (0 to 90): ", [str(i) for i in range(91)])
    latitude_minutes = Validate_Input("Enter latitude minutes' (0 to 59): ", [str(i) for i in range(60)])
    latitude_seconds = Validate_Input("Enter latitude seconds\" (0 to 59): ", [str(i) for i in range(60)])

    # Prompt the user for latitude hemisphere (N/S)
    latitude_hemisphere = Validate_Input("Enter latitude hemisphere (N or S): ", ['N', 'S'], 
                                         error_message = "Invalid input. Please enter \"N\" or \"S\"")

    # Prompt the user for longitude DMS coordinates
    longitude_degrees = Validate_Input("Enter longitude degrees° (0 to 180): ", [str(i) for i in range(181)])
    longitude_minutes = Validate_Input("Enter longitude minutes' (0 to 59): ", [str(i) for i in range(60)])
    longitude_seconds = Validate_Input("Enter longitude seconds\" (0 to 59): ", [str(i) for i in range(60)])

    # Prompt the user for longitude hemisphere (E/W)
    longitude_hemisphere = Validate_Input("Enter longitude hemisphere (E or W): ", ['E', 'W'], 
                                          error_message = "Invalid input. Please enter \"E\" or \"W\"")

    # Convert latitude DMS to DD
    latitude_decimal_degrees = DMS_to_DD(int(latitude_degrees), int(latitude_minutes), int(latitude_seconds))
    if latitude_hemisphere == 'S':
        latitude_decimal_degrees = -latitude_decimal_degrees

    # Convert longitude DMS to DD
    longitude_decimal_degrees = DMS_to_DD(int(longitude_degrees), int(longitude_minutes), int(longitude_seconds))
    if longitude_hemisphere == 'W':
        longitude_decimal_degrees = -longitude_decimal_degrees

    # Print the result
    print("\nCopy & paste DD coordinates into a GIS:")
    print(latitude_decimal_degrees, longitude_decimal_degrees, "\n")

if __name__ == "__main__":
    Convert_Coordinates() # calls the main method convert_coordinates()

"""
Latitude:
Degree° values range: [-90, 90]
Minute' values range: [0, 59]
Second" values range: [0, 59]
Negative values: Southern Hemisphere (south of the equator)
Positive values: Northern Hemisphere (north of the equator)
0 degrees: Equator

Longitude:
Degree° values domain: [-180, 180]
Minute' values domain: [0, 59]
Second" values domain: [0, 59]
Negative values: Western Hemisphere (west of the prime meridian)
Positive values: Eastern Hemisphere (east of the prime meridian)
0 degrees: Prime Meridian (passes through Greenwich, London)
"""