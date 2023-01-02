from project.car.car import Car


class SportsCar(Car):
    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value in range(400, 601):
            self.__speed_limit = value
        else:
            raise ValueError(f"Invalid speed limit! Must be between 400 and 600!")
