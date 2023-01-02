# from abc import ABC, abstractmethod
# from oop.polimorfism.exercise.project1.project.animals.animal import Animal, Mammal

from project.animals.animal import Mammal
from project.car import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):

    can_eat = ["Vegetable", "Fruit"]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Squeak"

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in Mouse.can_eat:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += food.quantity * 0.10
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):
    can_eat = ["Meat"]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Woof!"

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in Dog.can_eat:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += food.quantity * 0.40
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Cat(Mammal):
    can_eat = ["Vegetable", "Meat"]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Meow"

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in Cat.can_eat:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Tiger(Mammal):
    can_eat = ["Meat"]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"ROAR!!!"

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in Tiger.can_eat:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += food.quantity *  1
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
