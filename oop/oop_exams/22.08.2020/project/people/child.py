class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost
        # self.toys_cost = toys_cost
        result = food_cost + sum([el for el in toys_cost])
        self.cost = result


