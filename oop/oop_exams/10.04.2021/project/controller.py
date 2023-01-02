# from project.aquarium.freshwater_aquarium import FreshwaterAquarium
# from project.aquarium.saltwater_aquarium import SaltwaterAquarium
# from project.decoration.decoration_repository import DecorationRepository
# from project.decoration.ornament import Ornament
# from project.decoration.plant import Plant
# from project.fish.freshwater_fish import FreshwaterFish
# from project.fish.saltwater_fish import SaltwaterFish
#
#
# class Controller:
#     def __init__(self):
#         self.decorations_repository = DecorationRepository()
#         self.aquariums = []
#
#     def add_aquarium(self, aquarium_type: str, aquarium_name: str):
#         if aquarium_type != "FreshwaterAquarium" and aquarium_type != "SaltwaterAquarium":
#             return f"Invalid aquarium type."
#
#         if aquarium_type == "FreshwaterAquarium":
#             new_aqua = FreshwaterAquarium(aquarium_name)
#             self.aquariums.append(new_aqua)
#         else:
#             new_aqua = SaltwaterAquarium(aquarium_name)
#             self.aquariums.append(new_aqua)
#         return f"Successfully added {aquarium_type}."
#
#     def add_decoration(self, decoration_type: str):
#         if decoration_type != "Ornament" and decoration_type != "Plant":
#             return f"Invalid decoration type."
#
#         if decoration_type == "Ornament":
#             new_dec = Ornament()
#             self.decorations_repository.add(new_dec)
#         else:
#             new_dec = Plant()
#             self.decorations_repository.add(new_dec)
#         return f"Successfully added {decoration_type}."
#
#     def insert_decoration(self, aquarium_name: str, decoration_type: str):
#         decor = DecorationRepository.find_by_type(self.decorations_repository, decoration_type)
#
#         if not decor:
#             return f"There isn't a decoration of type {decoration_type}."
#
#         aquarium = Controller.find_by_name_aquarium(self, aquarium_name, self.aquariums)
#
#         if aquarium:
#             aquarium.decorations.append(decor)
#             DecorationRepository.remove(self.decorations_repository, decor)
#             return f"Successfully added {decoration_type} to {aquarium_name}."
#
#     def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
#         if fish_type != "FreshwaterFish" and fish_type != "SaltwaterFish":
#             return f"There isn't a fish of type {fish_type}."
#
#         aquarium = Controller.find_by_name_aquarium(self, aquarium_name, self.aquariums)
#
#         if len(aquarium.fish) + 1 > aquarium.capacity:
#             return f"Not enough capacity."
#
#         if fish_type == "FreshwaterFish":
#             new_fish = FreshwaterFish(fish_name, fish_species, price)
#             if new_fish.can_live != aquarium.__class__.__name__:
#                 return f"Water not suitable."
#             aquarium.add_fish(new_fish)
#         else:
#             new_fish = SaltwaterFish(fish_name, fish_species, price)
#             if new_fish.can_live != aquarium.__class__.__name__:
#                 return f"Water not suitable."
#             aquarium.add_fish(new_fish)
#         return f"Successfully added {fish_type} to {aquarium_name}."
#
#     def feed_fish(self, aquarium_name: str):
#         aquarium = Controller.find_by_name_aquarium(self, aquarium_name, self.aquariums)
#         counter = 0
#         for x in aquarium.fish:
#             x.feed()
#             counter += 1
#         return f"Fish fed: {counter}"
#
#     def calculate_value(self, aquarium_name: str):
#         aquarium = Controller.find_by_name_aquarium(self, aquarium_name, self.aquariums)
#         if aquarium:
#             total = 0
#             for x in aquarium.fish:
#                 total += x.price
#
#             for x in aquarium.decorations:
#                 total += x.price
#
#             return f"The value of Aquarium {aquarium_name} is {total:.2f}."
#
#     def report(self):
#         res = []
#         for ppp in self.aquariums:
#             res.append(ppp.__str__())
#         return '\n'.join(res)
#
#     @staticmethod
#     def find_by_name_aquarium(self, aquarium_name, list_aquariums):
#         for x in list_aquariums:
#             if x.name == aquarium_name:
#                 return x
#
#
# a = Controller()
# p = FreshwaterAquarium("f")
# pnat = Plant()
# orn = Ornament()
# p.decorations = [pnat, orn]
# a.aquariums = [p]
# b = DecorationRepository()
# a.decorations_repository = b
# w = Ornament()
# b.decorations = [w]
#
# # print(a.insert_decoration("f", w.__class__.__name__))
# # print(a.calculate_value("f"))
# print(a.report())

from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type != "FreshwaterAquarium" and aquarium_type != "SaltwaterAquarium":
            return f"Invalid aquarium type."

        if aquarium_type == "FreshwaterAquarium":
            new_aqua = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(new_aqua)
        else:
            new_aqua = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(new_aqua)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type != "Ornament" and decoration_type != "Plant":
            return f"Invalid decoration type."

        if decoration_type == "Ornament":
            new_dec = Ornament()
            self.decorations_repository.add(new_dec)
        else:
            new_dec = Plant()
            self.decorations_repository.add(new_dec)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decor = DecorationRepository.find_by_type(self.decorations_repository, decoration_type)

        if not decor:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = Controller.find_by_name_aquarium(self, aquarium_name, self.aquariums)

        if aquarium:
            aquarium.decorations.append(decor)
            # DecorationRepository.remove(self.decorations_repository, decor)
            for x in self.decorations_repository.decorations:
                if x == decor:
                    self.decorations_repository.decorations.remove(decor)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type != "FreshwaterFish" and fish_type != "SaltwaterFish":
            return f"There isn't a fish of type {fish_type}."

        aquarium = Controller.find_by_name_aquarium(self, aquarium_name, self.aquariums)

        if len(aquarium.fish) + 1 > aquarium.capacity:
            return f"Not enough capacity."

        if fish_type == "FreshwaterFish":
            new_fish = FreshwaterFish(fish_name, fish_species, price)
            if new_fish.can_live != aquarium.__class__.__name__:
                return f"Water not suitable."
            aquarium.fish.append(new_fish)
        else:
            new_fish = SaltwaterFish(fish_name, fish_species, price)
            if new_fish.can_live != aquarium.__class__.__name__:
                return f"Water not suitable."
            aquarium.fish.append(new_fish)
        return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        aquarium = Controller.find_by_name_aquarium(self, aquarium_name, self.aquariums)
        if aquarium is None:
            return
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = Controller.find_by_name_aquarium(self, aquarium_name, self.aquariums)
        if aquarium is "None":
            return
        if aquarium:
            total = 0
            for x in aquarium.fish:
                total += x.price

            for x in aquarium.decorations:
                total += x.price

            return f"The value of Aquarium {aquarium_name} is {total:.2f}."

    def report(self):
        res = []
        for ppp in self.aquariums:
            res.append(ppp.__str__())
        return '\n'.join(res)
        # output = []
        # for aquarium in self.aquariums:
        #     output.append(str(aquarium))
        # return os.linesep.join(output)

    @staticmethod
    def find_by_name_aquarium(self, aquarium_name, list_aquariums):
        for x in list_aquariums:
            if x.name == aquarium_name:
                return x
