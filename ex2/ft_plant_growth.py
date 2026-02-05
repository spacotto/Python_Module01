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

    def grow(self) -> None:
        """Increases the plant's height by its unique growth rate."""
        self.height += self.growth

    def aging(self) -> None:
        """Increases the plant's age by 7 days (one week)."""
        self.age += 7

    def get_info(self) -> str:
        """Returns a formatted string of the plant's current status."""
        diff = self.height - self.initial_height
        h_str: str = f"{self.height}cm"
        a_str: str = f"{self.age} days"
        g_str: str = f"+{diff} cm"
        return f" {self.name:<13}{h_str:<13}{a_str:<13}{g_str:<13}"

    def display_info(self) -> None:
        """Displays the current status of the plant."""
        print(get_info())


def display_header(current_week: int) -> None:
    """
    Displays the registry header.
    """
    # ANSI Colors
    white = "\033[1;97m"
    reset = "\033[0m"

    # Columns titles
    c1, c2, c3, c4 = "Name", "Height", "Age", "Growth"

    # Prints register header
    print(f"\n{white} 🌱 Garden Plant Registry: Week {current_week} 🌱{reset}\n")
    print(f" {white}{c1:<13}{c2:<13}{c3:<13}{c4:<13}{reset}")
    print(" --------------------------------------------------------")


def main() -> None:
    """Simulates a week of growth for the garden."""
    # Garden plants stored in a list
    garden: list[Plant] = [
        Plant("Rose", 25, 30, 5),
        Plant("Sunflower", 80, 45, 6),
        Plant("Cactus", 15, 120, 2)
    ]

    # Initial status display
    current_week = 1
    display_header(current_week)
    for p in garden:
        p.display_info()

    # Simulates growth
    start_week = 2
    weeks_to_simulate = 4
    for current_week in range(start_week, weeks_to_simulate + 1):
        display_header(current_week)

        for p in garden:
            p.grow()
            p.aging()

        for p in garden:
            p.display_info()

    print(" ")


if __name__ == "__main__":
    main()    
