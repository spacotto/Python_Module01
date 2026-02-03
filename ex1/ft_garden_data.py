#!/usr/bin/env python3
"""
Simulate plant growth and aging in a digital garden.
"""


class Plant:
    """
    A class representing a plant that can grow and age.
    """
    def __init__(self, name: str, height: int, age: int, growth: int) -> None:
        """Initializes the plant with starting values."""
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.growth: int = growth
        # Track initial height for growth reporting
        self.initial_height: int = height

    def display_header(self) -> None;
    print(f"\n{white} 🌱 Garden Plant Registry: Day 1 🌱{reset}\n")
    print(f" {white}{c1:<13}{c2:<13}{c3:<13}{reset}")
    print(" --------------------------------------------------------")
    
	def grow(self) -> None:
        """Increases the plant's height by its unique growth rate."""
        self.height += self.growth

    def aging(self) -> None:
        """Increases the plant's age by 7 days (one week)."""
        self.age += 7

    def display_info(self) -> None:
        """Displays the current status of the plant."""
        h_str: str = f"{self.height}cm"
        a_str: str = f"{self.age} days"
        print(f" {self.name:<13}{h_str:<13}{a_str:<13}")

    def display_weekly_growth(self) -> None:
        """Displays the net growth of this specific plant."""
        diff = self.height - self.initial_height
        print(f" {self.name:<13} +{diff} cm")


if __name__ == "__main__":
    # ANSI Color codes
    white = "\033[1;97m"
    reset = "\033[0m"

    # Columns titles
    c1, c2, c3 = "Name", "Height", "Age"

    # Multiple plants constituting the garden 
    garden: list[Plant] = [
        Plant("Rose", 25, 30, 5),
        Plant("Sunflower", 80, 45, 6),
        Plant("Cactus", 15, 120, 2)
    ]

    # Initial status display
    for p in garden:
        p.display_info()

    # Simulates growth
    weeks_to_simulate = 2
    for current_week in range(1, weeks_to_simulate + 1):
        # FIX: Loop through each plant to call methods
        for p in garden:
            p.grow()
            p.aging()

        for p in garden:
            p.display_info()

        for p in garden:
            p.display_weekly_growth()

    print("\n --------------------------------------------------------")
    print(" End of Program\n")
