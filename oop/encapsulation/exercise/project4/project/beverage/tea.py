from project.beverage.hot_beverage import HotBeverage
# from oop.encapsulation.exercise.project4.project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)