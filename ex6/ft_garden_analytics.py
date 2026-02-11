#!/usr/bin/env python3
"""
Building a comprehensive Garden Analytics Platform.
"""


class Plant:
    """Base class for all plants"""
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age
        self.type: str = "Plant"

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        if age > 0:
            self.__age = age

    def grow(self, days=1) -> None:
        self.__age += days
        print(f"{self.__name} grew {days} day(s).")

    def get_info(self) -> str:
        age_str: str = f"{self.__age} days"
        return f" {self.__name:<15}{age_str:<15}"

    @staticmethod
    def get_plant_score() -> int:
        return 10


class FloweringPlant(Plant):
    """A plant that has a color and blooms"""

    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(name, age)
        self.__color = color
        self.type: str = "FloweringPlant"

    def get_color(self) -> str:
        return self.__color

    def bloom(self) -> None:
        print(f"\n 🌱 {self.get_name()} is blooming beautifully!")

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}{self.__color:<15}"

    @staticmethod
    def get_flowering_plant_score() -> int:
        """Base score for a FloweringPlant"""
        return 20


class PrizeFlower(FloweringPlant):
    """A flowering plant that socred prize points"""

    def __init__(self, name: str, age: int, color: str, prize_points: int) -> None:
        super().__init__(name, age, color)
        self.__prize_points = prize_points
        self.type: str = "PrizeFlower"

    def get_prize_points(self) -> int:
        return self.__prize_points

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}{self.__prize_points:<10}"

    @staticmethod
    def get__prize_flower_score() -> int:
        return 30

class Garden:
    """Container for Plant objects"""
    def __init__(self, garden_name: str, owner_name: str) -> None:
        self.garden_name = 
        self.owner_name = owner_name
        self.plants = []

class GardenManager:
    """Manages multiple gardens and provides analytics"""
    def __init__(self):
        self.network = {}

    def create_garden_network(self) -> None:
        self.network = {}

    def create_garden(self, garden_name: str) -> Garden:
        """Creates a Garden that had its owner's name"""
        new_garden = Garden(garden_name)
        self.network[garden_name] = new_garden
        return new_garden

    def add_plant(self, garden: str, plant_obj: Plant) -> None:
        """
        Retrieves the garden from the network and adds the plant.
        This allows access to both the owner's name and the plant's name.
        """
        if garden in self.network:
            target_garden = self.network[garden]
            
            target_garden.plants += [plant_obj]
            
            print(f"Added {plant_obj.get_name()} to {garden}'s garden")
        else:
            print(f"Error: No garden found for {garden}")


def main() -> None:
    """Initialize manager and network"""
    manager = GardenManager()
    manager.create_garden_network()

    """Create a Garden via the manager"""
    AliceGarden = manager.create_garden("Alice")

    """Instantiate plants"""
    oak = Plant("Oak Tree", 101)
    rose = FloweringPlant("Rose", 26, "Red")
    sunflower = PrizeFlower("Sunflower", 51, "Yellow", 10)

    """Add plants to the garden in the network"""
    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    manager.add_plant("Alice", sunflower)


if __name__ == "__main__":
    main()
