from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError(f"Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        total = 0
        for x in self.decorations:
            total += x.comfort
        return total

    def add_fish(self, fish):
        if fish.__class__.__name__ != "FreshwaterFish" and fish.__class__.__name__ != "SaltwaterFish":
            return
        if len(self.fish) + 1 <= self.capacity:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        return f"Not enough capacity."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for x in self.fish:
            x.eat()

    def __str__(self):
        result = f"{self.name}:" + "\n"
        if not self.fish:
            result += f"Fish: none" + "\n"
            result += f"Decorations: {len(self.decorations)}" + "\n"
            com = 0
            for x in self.decorations:
                com += x.comfort
            result += f"Comfort: {com}"
        else:
            result += f"Fish: {' '.join([x.name for x in self.fish])}" + "\n"
            result += f"Decorations: {len(self.decorations)}" + "\n"
            com = 0
            for x in self.decorations:
                com += x.comfort
            result += f"Comfort: {com}"
        return result
