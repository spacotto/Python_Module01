#!/usr/bin/env python3

"""
This program:
1. runs when executed directly
2. stores plant information in simple variables (name, height, age)
3. displays the plant information using print()
"""

def display_plant_info(name: str, height: int, age: int) -> None:
    """
    Displays the basic information of a plant in the garden.
    """
    # ANSI Color codes
    white   = "\033[1;97m"
    reset   = "\033[0m"

    # Printing
    print("Welcome to My Garden")
    print(f"Plant:  {name}")
    print(f"Height: {height}cm")
    print(f"Age:    {age} days")
    print("End of Program")


if __name__ == "__main__":
    # Internal variables to store plant data
    plant_name: str = "Rose"
    plant_height: int = 25
    plant_age: int = 30

    display_plant_info(plant_name, plant_height, plant_age)
