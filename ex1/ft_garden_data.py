#!/usr/bin/env python3

"""
This program track multiple plants with their information.
"""


def ft_garden_data(name: str, height: int, age: int) -> None:
    """
    Text goes here
    """
    print(f" {name:<13}{f'{height}cm':<13}{f'{age} days':<13}")

if __name__ == "__main__":
    
    # ANSI Color codes
    white = "\033[1;97m"
    reset = "\033[0m"

    # Columns titles
    c1 = "Name"
    c2 = "Height"
    c3 = "Age"
    
    # Fixed start of program print
    print(f"\n{white} 🌱 Garden Plant Registry 🌱{reset}\n")
    print(f" {white}{c1:<13}{c2:<13}{c3:<13}{reset}")
    print(" --------------------------------------------------------")

    # Add data entries
    ft_garden_data("Rose", 25, 30)
    ft_garden_data("Sunflower", 80, 45)
    ft_garden_data("Cactus", 15, 120)

    # Fixed end of program print
    print("\n --------------------------------------------------------")
    print(" End of Program\n")

