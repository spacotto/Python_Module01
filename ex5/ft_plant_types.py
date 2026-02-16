#!/usr/bin/env python3
"""
Implement Inheritance for specialised plant types.
"""


class Plant:
    """Base class for all garden plants."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialises common plant features."""
        self.type: str = "Plant"
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def display_details(self) -> None:
        """Base display for common attributes."""
        white, reset = "\033[1;97m", "\033[0m"
        print(f"\n {white}{'Name':<20}{reset}{self.name} ({self.type})")
        print(f" {white}{'Height':<20}{reset}{self.height}cm")
        print(f" {white}{'Age':<20}{reset}{self.age} days")


class Flower(Plant):
    """Specialised plant that can bloom."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Uses super() to initialize common attributes and adds color."""
        super().__init__(name, height, age)
        self.type: str = "Flower"
        self.color: str = color

    def bloom(self) -> None:
        """Displays a blooming message."""
        print(f"\n 🌱 {self.name} is blooming beautifully!")

    def display_details(self) -> None:
        white, reset = "\033[1;97m", "\033[0m"
        super().display_details()
        print(f" {white}{'Color':<20}{reset}{self.color}")
        self.bloom()


class Tree(Plant):
    """Specialised plant that provides shade."""
    def __init__(self, name: str, height: int, age: int,
                 diameter: int) -> None:
        """Adds trunk_diameter to the base plant."""
        super().__init__(name, height, age)
        self.type: str = "Tree"
        self.trunk_diameter: int = diameter

    def produce_shade(self) -> None:
        """Calculates and displays shade area."""
        shade_area = self.trunk_diameter * 1.5
        print(f"\n 🌱 {self.name} provides {shade_area} square meters of shade")

    def display_details(self) -> None:
        white, reset = "\033[1;97m", "\033[0m"
        super().display_details()
        print(f" {white}{'Diameter':<20}{reset}{self.trunk_diameter}cm")
        self.produce_shade()


class Vegetable(Plant):
    """Specialised plant for harvesting."""
    def __init__(self, name: str, h: int, a: int,
                 harvest_time: str, nutriscore: str) -> None:
        """Adds harvest season and nutritional value."""
        super().__init__(name, h, a)
        self.type: str = "Vegetable"
        self.harvest_season: str = harvest_time
        self.nutritional_value: str = nutriscore

    def harvest_info(self) -> None:
        """Displays nutritional information."""
        print(f"\n 🌱 {self.name} is rich in {self.nutritional_value}")

    def display_details(self) -> None:
        white, reset = "\033[1;97m", "\033[0m"
        super().display_details()
        print(f" {white}{'Harvest Season':<20}{reset}{self.harvest_season}")
        print(f" {white}{'Nutritional Value':<20}{reset}"
              f"{self.nutritional_value}")
        self.harvest_info()


def status_helper(plant_object: Plant) -> None:
    """Uses polymorphism to display any plant's status."""
    plant_object.display_details()
    print("\n " + "-" * 50)


def main() -> None:
    """Colors"""
    white = "\033[1;97m"
    reset = "\033[0m"

    """Printing"""
    print(f"\n {white}🌱 Garden Plant Types{reset}")
    print(" " + "-" * 50)

    rose = Flower("Rose", 25, 30, "Red")
    status_helper(rose)

    sunflower = Flower("Sunflower", 80, 45, "Yellow")
    status_helper(sunflower)

    oak = Tree("Oak", 500, 1825, 50)
    status_helper(oak)

    bonsai = Tree("Bonsai", 15, 3650, 5)
    status_helper(bonsai)

    tomato = Vegetable("Tomato", 80, 90, "Summer", "Vitamin C")
    status_helper(tomato)

    carrot = Vegetable("Carrot", 20, 70, "Autumn", "Vitamin A")
    status_helper(carrot)

    print(f" {white}🌱 End of Garden Plant Types List{reset}\n")


if __name__ == "__main__":
    main()
