# Author: Peyton J. Hall (C)
"""
This Python program converts Decimal Degree (DD) coordinates
to Degree Minute Second (DMS) coordinates, according to the
WGS84 datum of the Cartesian coordinate system.
"""

def DD_to_DMS(decimal_degrees, hemisphere):

    # Absolute value validates the user input algebraically
    decimal_degrees = abs(decimal_degrees)
    
    # Conversion Formula for d.d° to d°m's" = d = int(d.d°), m = int((d.d° - d) * 60), s = (d.d° - d - (m/60)) * 60
    degrees = int(decimal_degrees)
    decimal_minutes = (decimal_degrees - degrees) * 60
    minutes = int(decimal_minutes)
    seconds = (decimal_minutes - minutes) * 60
    
    # Return the DMS coordinates with hemisphere indicator
    return str(degrees) + '°' + str(minutes) + "'" + str(round(seconds, 2)) + '"' + hemisphere

def Validate_Input(prompt, range_start, range_end):
    valid_values = ', '.join(str(i) for i in range(range_start, range_end + 1))
    error_message = f"Invalid input. Please enter a valid value between {range_start} and {range_end} ({valid_values})."
    
    # Infinite loop continues prompts until a valid value is entered
    while True:
        try:
            value = float(input(prompt))  # Get user input as a float
            if not (range_start <= value <= range_end):  # Check if input falls in the range defined by the main method
                raise ValueError  # input is invalid
            return value  # return the validated input
        except ValueError:  # built-in exception
            print(error_message)

# main method
def Convert_Coordinates():
    print("Convert Decimal Degree (DD) coordinates to Degree Minute Second (DMS) coordinates.\n")

    # Prompt the user for latitude DD coordinates
    latitude_decimal_degrees = Validate_Input("Enter latitude in decimal degrees (-90 to 90): ", -90, 90)

    # Prompt the user for longitude DD coordinates
    longitude_decimal_degrees = Validate_Input("Enter longitude in decimal degrees (-180 to 180): ", -180, 180)

    # Convert latitude DD to DMS
    latitude_dms = DD_to_DMS(latitude_decimal_degrees, 'N' if latitude_decimal_degrees >= 0 else 'S')

    # Convert longitude DD to DMS
    longitude_dms = DD_to_DMS(longitude_decimal_degrees, 'E' if longitude_decimal_degrees >= 0 else 'W')

    # Print the result
    print("\nCopy & paste DMS coordinates into a GIS:")
    print(latitude_dms, longitude_dms, "\n")

if __name__ == "__main__":
    Convert_Coordinates()

"""
Latitude:
Decimal Degree° values range: [-90, 90]
Minute' and Second" values: Represented after the decimal point 
Negative values: Southern Hemisphere (south of the equator)
Positive values: Northern Hemisphere (north of the equator)
0 degrees: Equator

Longitude:
Decimal Degree° values domain: [-180, 180]
Minute' and Second" values: Represented after the decimal point 
Negative values: Western Hemisphere (west of the prime meridian)
Positive values: Eastern Hemisphere (east of the prime meridian)
0 degrees: Prime Meridian (passes through Greenwich, London)
"""
