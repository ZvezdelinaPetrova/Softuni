from project.cat import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []  # an empty list which will contain the players of the guild

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = ""
        if self.players:
            for pl in self.players:
                result += f"Guild: {pl.guild}" + "\n"
                result += f"{pl.player_info()}" + "\n"
            return result.strip()
        return f"Guild: {self.name}"
