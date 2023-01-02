# from oop.polimorfism.exercise.project1.project.animals.animal import Bird, Animal


from project.animals.animal import Bird


class Owl(Bird):

    can_eat = ["Meat"]

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return f"Hoot Hoot"

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in Owl.can_eat:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):

    can_eat = ["Vegetable", "Fruit", "Meat", "Seed"]

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return f"Cluck"

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in Hen.can_eat:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"