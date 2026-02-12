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

    def grow(self, days: int) -> None:
        self.__age += days
        print(f" {self.__name} grew {days} day(s).")

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
        self.__garden_name = garden_name
        self.__owner_name = owner_name
        self.plants = []

    def get_garden_name(self) -> str:
        return self.__garden_name

    def get_owner_name(self) -> str:
        return self.__owner_name


class GardenManager:
    """Manages multiple gardens and provides analytics"""
    def __init__(self):
        self.__network = [] 

    def create_garden_network(self) -> None:
        self.__network = []

    def create_garden(self, garden_name: str, owner_name: str) -> Garden:
        """Creates a Garden that had its owner's name"""
        new_garden = Garden(garden_name, owner_name)
        self.__network += [new_garden]
        return new_garden

    def add_plant(self, owner: str, garden: str, plant_obj: Plant) -> None:
        """
        Retrieves the garden list from the network list and adds the plant.
        """
        for target_garden in self.__network:
            """Check if the target Garden list is present in Networn list"""
            if target_garden.get_garden_name() == garden:
                target_garden.plants += [plant_obj]
                print(f" Added {plant_obj.get_name()} to {owner}'s garden")
                return
        print(f"Error: No garden found for {garden}")

    def grow_garden(self, garden_name: str, days: int) -> None:
        """Executes grow on all plants within a specific garden"""
        for target_garden in self.__network:
            if target_garden.get_garden_name() == garden_name:
                owner = target_garden.get_owner_name()
                print(f"\n 🌱 {owner} is helping all plants grow...")
                for plant in target_garden.plants:
                    plant.grow(days)
                return
        print(f"Error: Garden '{garden_name}' not found in network.")

    class GardenStats:
        """Nested helper class for calculating garden statistics"""
        def __init__(self, manager: 'GardenManager'):
            self.__manager = manager

        def display_plants_list(self, garden_name: str) -> None:
            """Displays the list of plants and their data in a target garden"""
            white = "\033[1;97m"
            reset = "\033[0m"
            c1, c2, c3, c4 = "Name", "Age", "Color", "Points"
            for target_garden in self._GardenStats__manager._GardenManager__network:
                """Searches for the target garden in the network"""
                if target_garden.get_garden_name() == garden_name:
                    print("\n 🌱 Plants in garden\n")
                    print(f" {white}{c1:<15}{c2:<15}{c3:<15}{c4:<15}{reset}")
                    print(" --------------------------------------------------------")
                    for plant in target_garden.plants:
                        print(plant.get_info())
                    return
            print(f"Error: Garden '{garden_name}' not found for report.")

        def count_plants(self, garden_name: str) -> int:
            """Calculates how many plants are in the garden"""
            plants = 0
            for target_garden in self.__manager._GardenManager__network:
                if target_garden.get_garden_name() == garden_name:
                    for _ in target_garden.plants:
                        plants += 1
            return plants

        def display_garden_stats(self, garden_name: str) -> None:
            plants_added = self.count_plants(garden_name)
            print(f" Plants added: {plants_added}")

        def display_garden_report(self, garden_name: str) -> None:
            """Displays all the stats of a target Garden"""
            white = "\033[1;97m"
            reset = "\033[0m"
            """Find the owner of the Garden"""
            owner_name = "Unknown"
            for target_garden in self.__manager._GardenManager__network:
                if target_garden.get_garden_name() == garden_name:
                    owner_name = target_garden.get_owner_name()
                    break
            """Display the report"""
            print(f"\n{white} 🌱 {owner_name}'s Garden Report 🌱{reset}")
            self.display_plants_list(garden_name)
            print(f"\n 🌱 {owner_name}'s Garden Stats")
            self.display_garden_stats(garden_name)
            print(" ")


def main() -> None:
    white = "\033[1;97m"
    reset = "\033[0m"

    """Initialize manager, network, and stats"""
    manager = GardenManager()
    manager.create_garden_network()
    stats = GardenManager.GardenStats(manager)

    """Create a Garden via the manager"""
    AliceGarden = manager.create_garden("Wonderland", "Alice")

    """Instantiate plants"""
    oak = Plant("Oak Tree", 101)
    rose = FloweringPlant("Rose", 26, "Red")
    sunflower = PrizeFlower("Sunflower", 51, "Yellow", 10)

    """Start Garden Demo"""
    print(f"\n{white} 🌱 Garden Management System Demo 🌱{reset}\n")

    """Add plants to the garden in the network"""
    manager.add_plant("Alice", "Wonderland", oak)
    manager.add_plant("Alice", "Wonderland", rose)
    manager.add_plant("Alice", "Wonderland", sunflower)

    """Execute grow on all the plants in target Garden"""
    manager.grow_garden("Wonderland", 1)

    """Garden Report"""
    stats.display_garden_report("Wonderland")

if __name__ == "__main__":
    main()
