#!/usr/bin/env python3
"""
Organise garden data
"""

class Plant:
    """
    A class representing a plant that can grow and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the plant with values."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def display_header(self) -> None:
	    # ANSI Color codes
        white = "\033[1;97m"
        reset = "\033[0m"

		# Columns titles
        c1, c2, c3 = "Name", "Height", "Age"

		# Print header
        print(f"\n{white} 🌱 Garden Plant Registry: Day 1 🌱{reset}\n")
        print(f" {white}{c1:<13}{c2:<13}{c3:<13}{reset}")
        print(" --------------------------------------------------------")

    def display_info(self) -> None:
        """Displays the current status of the plant."""
        h_str: str = f"{self.height}cm"
        a_str: str = f"{self.age} days"
        print(f" {self.name:<13}{h_str:<13}{a_str:<13}")


if __name__ == "__main__":
    # Multiple plants constituting the garden 
    garden: list[Plant] = [
        Plant("Rose", 25, 30, 5),
        Plant("Sunflower", 80, 45, 6),
        Plant("Cactus", 15, 120, 2)
