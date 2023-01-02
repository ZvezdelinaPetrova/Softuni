from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.driver import Driver
from project.car.sports_car import SportsCar
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type != "MuscleCar" and car_type != "SportsCar":
            return

        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar":
            new_car = MuscleCar(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

        if car_type == "SportsCar":
            new_car = SportsCar(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = Controller.find_object(self, driver_name, self.drivers)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type != "MuscleCar" and car_type != "SportsCar":
            raise Exception(f"Car {car_type} could not be found!")

        cars_that_type = []
        # cars_that_type = [x for x in self.cars if x == car_type]
        for x in self.cars:
            if x.__class__.__name__ == car_type:
                cars_that_type.append(x)

        # if not cars_that_type:
        #     raise Exception(f"Car {car_type} could not be found!")

        available_cars_that_are_not_taken = []
        for x in cars_that_type:
            if not x.is_taken:
                available_cars_that_are_not_taken.append(x)

        if not available_cars_that_are_not_taken:
            raise Exception(f"Car {car_type} could not be found!")

        if (driver.car is not None) and available_cars_that_are_not_taken:
            old_one = driver.car
            last_car = available_cars_that_are_not_taken[-1]
            driver.car = last_car
            old_one.is_taken = False
            last_car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_one.model} to {last_car.model}."
        if (driver.car is None) and available_cars_that_are_not_taken:
            last_car = available_cars_that_are_not_taken[-1]
            driver.car = last_car
            last_car.is_taken = True
            return f"Driver {driver_name} chose the car {last_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = Controller.find_object(self, driver_name, self.drivers)

        race_name_found = [x for x in self.races if x.name == race_name]
        if not race_name_found:
            raise Exception(f"Race {race_name} could not be found!")
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        for x in self.races:
            if x == race_name_found[0]:
                if driver in x.drivers:
                    return f"Driver {driver_name} is already added in {race_name} race."
            x.drivers.append(driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race_name_found = [x for x in self.races if x.name == race_name]
        if not race_name_found:
            raise Exception(f"Race {race_name} could not be found!")
        for x in self.races:
            if x == race_name_found[0]:
                if len(x.drivers) < 3:
                    raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

            sorted_speed_limit = sorted(x.drivers, key=lambda x: x.car.speed_limit)
            winners_1 = sorted_speed_limit[-1]
            winners_2 = sorted_speed_limit[-2]
            winners_3 = sorted_speed_limit[-3]
            winners = [winners_1, winners_2, winners_3]

            for winner in winners:
                winner.number_of_wins += 1
            result = ""
            for d in winners:
                result += f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}." + "\n"
            return result.strip()

    def find_object(self, d_name, list_with_objects):
        for obj in list_with_objects:
            if obj.name == d_name:
                return obj
