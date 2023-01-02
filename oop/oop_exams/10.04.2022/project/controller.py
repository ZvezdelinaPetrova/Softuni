from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply
from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        new_l = []
        for p in args:
            if p in self.players:
                continue
            self.players.append(p)
            new_l.append(p)
        return f"Successfully added: {', '.join([x.name for x in new_l])}"

    def add_supply(self, *args):
        for x in args:
            self.supplies.append(x)

    def sustain(self, player_name: str, sustenance_type: str):
        player = Controller.find_object(self, player_name, self.players)

        if not player:
            return

        if sustenance_type != "Food" and sustenance_type != "Drink":
            return

        if player.stamina >= 100:
            return f"{player_name} have enough stamina."

        if sustenance_type == "Food":
            is_there_a_food = [x for x in self.supplies if x.__class__.__name__ == "Food"]
            if not is_there_a_food:
                raise Exception(f"There are no food supplies left!")
            last_supply = is_there_a_food[-1]
            if player.stamina + last_supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += last_supply.energy
            self.supplies.remove(last_supply)
            return f"{player_name} sustained successfully with {last_supply.name}."

        if sustenance_type == "Drink":
            is_there_a_drink = [x for x in self.supplies if x.__class__.__name__ == "Drink"]
            if not is_there_a_drink:
                raise Exception(f"There are no drink supplies left!")
            last_supply = is_there_a_drink[-1]
            if player.stamina + last_supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += last_supply.energy
            self.supplies.remove(last_supply)
            return f"{player_name} sustained successfully with {last_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player = Controller.find_object(self, first_player_name, self.players)
        player_2 = Controller.find_object(self, second_player_name, self.players)
        if player.stamina == 0 and player_2.stamina == 0:
            result = f"Player {first_player_name} does not have enough stamina." + "\n"
            result += f"Player {second_player_name} does not have enough stamina."
            return result

        if player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."

        if player_2.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if player.stamina < player_2.stamina:
            player_2.stamina -= player.stamina / 2
            if player_2.stamina <= 0:
                player_2.stamina = 0
                return f"Winner: {player.name}"
            player.stamina -= player_2.stamina / 2
            if player.stamina <= 0:
                player.stamina = 0
                return f"Winner: {player_2.name}"
        else:
            player.stamina -= player_2.stamina / 2
            if player.stamina <= 0:
                player.stamina = 0
                return f"Winner: {player_2.name}"
            player_2.stamina -= player.stamina / 2
            if player_2.stamina <= 0:
                player_2.stamina = 0
                return f"Winner: {player.name}"
        if player.stamina < player_2.stamina:
            return f"Winner: {player_2.name}"
        else:
            return f"Winner: {player.name}"

    def next_day(self):
        for x in self.players:
            if x.stamina - (x.age * 2) < 0:
                x.stamina = 0
            else:
                x.stamina -= (x.age * 2)

        for y in self.players:
            if self.supplies:
                for x in range(len(self.supplies) - 1, -1, -1):
                    if self.supplies[x].__class__.__name__ == "Food":
                        item = self.supplies.pop(x)
                        if y.stamina + item.energy > 100:
                            y.stamina = 100
                        else:
                            y.stamina += item.energy
                        break
            else:
                break

        for y in self.players:
            if self.supplies:
                for x in range(len(self.supplies) - 1, -1, -1):
                    if self.supplies[x].__class__.__name__ == "Drink":
                        item = self.supplies.pop(x)
                        if y.stamina + item.energy > 100:
                            y.stamina = 100
                        else:
                            y.stamina += item.energy
                        break
            else:
                break

    def __str__(self):
        result = ""
        for x in self.players:
            result += f"{x.__str__()}" + "\n"
        for x in self.supplies:
            result += f"{x.details()}" + "\n"
        return result.strip()

    def find_object(self, p_name, list_with_objects):
        for obj in list_with_objects:
            if obj.name == p_name:
                return obj


