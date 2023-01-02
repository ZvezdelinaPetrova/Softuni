from project.beverage.beverage import Beverage
# from oop.encapsulation.exercise.project4.project.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)
