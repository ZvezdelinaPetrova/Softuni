from project.car.car import Car


class MuscleCar(Car):
    min_s = 250
    max_s = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value in range(250, 451):
            self.__speed_limit = value
        else:
            raise ValueError(f"Invalid speed limit! Must be between 250 and 450!")

