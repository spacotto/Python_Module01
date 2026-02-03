#!/usr/bin/env python3
"""
Implementing an efficient Plant Factory using class initialisation.
"""


class Plant:
    """
    A class representing a plant with immediate initialisation.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialises the plant with starting values.
        Requirement: Each plant should be ready to use immediately.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def display_creation(self) -> None:
        """
        Displays the plant's data in the 'Factory Output' format.
        """
        # Formats the string to match the 'Created: Name (Xcm, Y days)' style
        info: str = f"({self.height}cm, {self.age} days)"
        print(f"Created: {self.name:<10} {info}")


if __name__ == "__main__":
    """
    Main function to simulate the Plant Factory.
    """
    print("=== Plant Factory Output ===")
    
    # Requirement: Create at least 5 different plants 
    # We use a list to streamline the storage and display process.
    factory_batch: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    # Iterate through the batch to display them
    for plant in factory_batch:
        plant.display_creation()

    print(f"Total plants created: {len(factory_batch)}")
