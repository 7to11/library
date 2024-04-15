#......................................................................
#library math
#kohen johnsotn 
#2024-04-25
#......................................................................


#imports
import math
import custom_module
import external_library

# Main 
def main():
    # Using math module to do math
    radius = 10
    area = math.pi * math.pow(radius, 2)
    circumference = 2 * math.pi * radius
    print(f"Area of the circle: {area}")
    print(f"Circumference of the circle: {circumference}")

    # Using custom module to perform math
    result = custom_module.calculate(10, 5)
    print(f"Result of custom calculation: {result}")

    # Using the library to access variables and functions
    print(f"Variable from external library: {external_library.external_variable}")
    print(f"Function result from external library: {external_library.external_function()}")

