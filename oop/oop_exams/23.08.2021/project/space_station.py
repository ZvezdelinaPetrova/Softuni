from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from collections import deque


class SpaceStation:
    def __init__(self):
        self.astronaut_repository = AstronautRepository()
        self.planet_repository = PlanetRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type != "Biologist" and astronaut_type != "Geodesist" and astronaut_type != "Meteorologist":
            raise Exception(f"Astronaut type is not valid!")

        for a in self.astronaut_repository.astronauts:
            if a.name == name:
                return f"{name} is already added."
        if astronaut_type == "Biologist":
            new_astronaut = Biologist(name)
            self.astronaut_repository.astronauts.append(new_astronaut)
            return f"Successfully added {astronaut_type}: {name}."
        if astronaut_type == "Geodesist":
            new_astronaut = Geodesist(name)
            self.astronaut_repository.astronauts.append(new_astronaut)
            return f"Successfully added {astronaut_type}: {name}."
        if astronaut_type == "Meteorologist":
            new_astronaut = Meteorologist(name)
            self.astronaut_repository.astronauts.append(new_astronaut)
            return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        for a in self.planet_repository.planets:
            if a.name == name:
                return f"{name} is already added."
        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        self.planet_repository.planets.append(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        for a in self.astronaut_repository.astronauts:
            if a.name == name:
                self.astronaut_repository.astronauts.remove(a)
                return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception(f"Invalid planet name!")

        astronauts = self.astronaut_repository.find_astronauts_for_mission(5, 30)

        if len(astronauts) == 0:
            raise Exception(f"You need at least one astronaut to explore the planet!")

        counter = 0
        for astronaut in astronauts:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            counter += 1

        if not planet.items:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {counter} astronauts participated in collecting items."
        else:
            self.unsuccessful_missions += 1
            return f"Mission is not completed."

    def report(self):
        result = ""
        result += f"{self.successful_missions} successful missions!" + "\n"
        result += f"{self.unsuccessful_missions} missions were not completed!" + "\n"
        result += f"Astronauts' info:" + "\n"
        for x in self.astronaut_repository.astronauts:
            result += f"Name: {x.name}" + "\n"
            result += f"Oxygen: {x.oxygen}" + "\n"
            result += f"Backpack items: {', '.join(x for x in x.backpack) if x.backpack else 'none'}" + "\n"
        return result.strip()



