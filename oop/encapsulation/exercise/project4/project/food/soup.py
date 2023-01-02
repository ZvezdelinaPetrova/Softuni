# from oop.encapsulation.exercise.project4.project.food.starter import Starter

from project.car.starter import Starter


class Soup(Starter):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)
