#!/usr/bin/env python3
"""
Building a comprehensive Garden Analytics Platform.
"""


class Plant:
    def __init__(self, name: str, age: int):
        self.__name = name
        if age >= 0:
            self.__age = age
        else:
            self.__age = 0
            print(f" Error: Invalid age {age} for {name}. Set to 0.")

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
        else:
            print(f" Error: Invalid age {age}. Age not updated.")

    def grow(self, days: int) -> None:
        self.__age += days
        print(f" {self.__name} grew {days} day(s).")

    def get_score(self) -> int:
        return 10

    def get_type(self) -> str:
        return "Plant"

    def get_color(self) -> str:
        return "-"

    def get_prize_points(self) -> int:
        return 0


class FloweringPlant(Plant):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.__color = color

    def bloom(self) -> None:
        print(f"\n 🌱 {self.get_name()} is blooming beautifully!")

    def get_score(self) -> int:
        return 20

    def get_type(self) -> str:
        return "FloweringPlant"

    def get_color(self) -> str:
        return self.__color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, age: int, color: str,
                 prize_points: int):
        super().__init__(name, age, color)
        self.__prize_points = prize_points

    def get_score(self) -> int:
        return 20 + self.__prize_points

    def get_type(self) -> str:
        return "PrizeFlower"

    def get_prize_points(self) -> int:
        return self.__prize_points


class Garden:
    def __init__(self, name: str, owner: str):
        self.__name = name
        self.__owner = owner
        self.__plants = []
        self.__total_growth = 0

    def get_name(self) -> str:
        return self.__name

    def get_owner(self) -> str:
        return self.__owner

    def add_plant(self, plant: Plant) -> None:
        self.__plants = self.__plants + [plant]

    def get_plants(self) -> list:
        return self.__plants

    def get_total_growth(self) -> int:
        return self.__total_growth

    def add_growth(self, days: int) -> None:
        self.__total_growth += days

    def calculate_score(self) -> int:
        total = 0
        for plant in self.__plants:
            total += plant.get_score()
            total += plant.get_age()
        return total


class GardenManager:
    def __init__(self):
        self.__network = []

    def create_garden_network(cls):
        return cls()

    create_garden_network = classmethod(create_garden_network)

    def bold_str(text: str) -> str:
        """A function making strings of text bold."""
        w, r = "\033[1;97m", "\033[0m"
        return f"{w}{text}{r}"

    bold_str = staticmethod(bold_str)

    def add_garden(self, garden: Garden) -> Garden:
        self.__network = self.__network + [garden]
        return garden

    def get_network(self) -> list:
        return self.__network

    def get_garden_by_owner(self, owner: str) -> Garden:
        for garden in self.__network:
            if garden.get_owner() == owner:
                return garden
        return None

    def add_plant(self, owner: str, plant_type: str, name: str,
                  age: int, **kwargs) -> None:
        """
        Add a plant to a garden identified by owner name.
        Use kwargs keyword for variadic arguments (dictionary of keyword args).
        """
        garden = self.get_garden_by_owner(owner)
        if not garden:
            return

        plant = None

        if plant_type == "Plant":
            plant = Plant(name, age)
        elif plant_type == "FloweringPlant":
            color = kwargs["color"] if "color" in kwargs else ""
            plant = FloweringPlant(name, age, color)
        elif plant_type == "PrizeFlower":
            color = kwargs["color"] if "color" in kwargs else ""
            prize_points = (kwargs["prize_points"]
                            if "prize_points" in kwargs else 0)
            plant = PrizeFlower(name, age, color, prize_points)

        if plant:
            garden.add_plant(plant)
            print(f" Added {name} to {garden.get_owner()}'s garden")

    def grow_garden(self, owner: str, days: int) -> None:
        garden = self.get_garden_by_owner(owner)
        if not garden:
            return

        print(f"\n 🌱 {owner} is helping all plants grow...")
        for plant in garden.get_plants():
            plant.grow(days)
            garden.add_growth(days)

    def generate_network_report(self) -> None:
        title = GardenManager.bold_str(" 🌱 Network Analytics Report 🌱")
        print(f"\n{title}\n")
        print(f" {'Garden':<20} {'Owner':<20} {'Score':<20}")
        print(" " + "-" * 60)

        for garden in self.__network:
            score = garden.calculate_score()
            name = garden.get_name()
            owner = garden.get_owner()
            print(f" {name:<20} {owner:<20} {score:<20}")

        print(" " + "-" * 60)
        count = self.GardenStats.count_gardens(self.__network)
        print(f" Total gardens managed: {count}\n")

    def generate_garden_report(self, owner: str) -> None:
        garden = self.get_garden_by_owner(owner)
        if garden:
            stats = self.GardenStats(garden)
            stats.generate_report()
        else:
            print(f" Garden for {owner} not found in network.")

    class GardenStats:
        def __init__(self, garden: Garden):
            self.__garden = garden

        def generate_report(self) -> None:
            owner = self.__garden.get_owner()
            title = GardenManager.bold_str(f" 🌱 {owner}'s Garden Report 🌱")
            print(f"\n{title}\n")
            headers = f" {'Plant':<15} {'Age':<15} {'Color':<15}"
            headers += f" {'Points':<15}"
            print(headers)
            print(" " + "-" * 60)

            self.display_plants_list()

            added = self.stats_added_plants()
            growth = self.stats_total_growth()
            print(f"\n Plants added: {added}, Total growth: "
                  f"{growth} day(s)")

            types = self.stats_plant_types()
            print(f" Plant types: {types['Plant']} regular, "
                  f"{types['FloweringPlant']} flowering, "
                  f"{types['PrizeFlower']} prize flowers")

        def display_plants_list(self) -> None:
            for plant in self.__garden.get_plants():
                name = plant.get_name()
                age = f"{plant.get_age()} days"
                color = plant.get_color()
                prize_pts = plant.get_prize_points()
                prize = prize_pts if prize_pts > 0 else ""

                print(f" {name:<15} {age:<15} {color:<15} "
                      f"{str(prize):<15}")

        def stats_added_plants(self) -> int:
            count = 0
            for plant in self.__garden.get_plants():
                count += 1
            return count

        def stats_total_growth(self) -> int:
            return self.__garden.get_total_growth()

        def stats_plant_types(self) -> dict:
            types = {"Plant": 0, "FloweringPlant": 0,
                     "PrizeFlower": 0}

            for plant in self.__garden.get_plants():
                plant_type = plant.get_type()
                types[plant_type] += 1

            return types

        def count_gardens(network: list) -> int:
            count = 0
            for garden in network:
                count += 1
            return count


def main():
    title = GardenManager.bold_str(" 🌱 Garden Management System Demo 🌱")
    print(f"\n{title}\n")

    """Create manager"""
    manager = GardenManager.create_garden_network()

    """Add gardens"""
    manager.add_garden(Garden("Wonderland", "Alice"))
    manager.add_garden(Garden("Backyard", "Bob"))

    """Add plants to Alice's garden"""
    manager.add_plant("Alice", "Plant", "Oak Tree", 101)
    manager.add_plant("Alice", "FloweringPlant", "Rose", 26,
                      color="Red")
    manager.add_plant("Alice", "PrizeFlower", "Sunflower", 51,
                      color="Yellow", prize_points=11)
    print(" ")

    """Add plants to Bob's garden"""
    manager.add_plant("Bob", "Plant", "Ash", 50)
    manager.add_plant("Bob", "FloweringPlant", "Tulip", 30,
                      color="Pink")
    manager.add_plant("Bob", "PrizeFlower", "Orchid", 40,
                      color="Purple", prize_points=20)

    """Grow Alice's garden by 1 day"""
    manager.grow_garden("Alice", 1)

    """Generate garden report"""
    manager.generate_garden_report("Alice")

    """Generate network report"""
    manager.generate_network_report()


if __name__ == "__main__":
    main()
