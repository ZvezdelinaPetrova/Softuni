from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if any([x for x in self.pokemons if x.name == pokemon.name]):
            return 'This pokemon is already caught'

        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    # def add_pokemon(self, pokemon):
    #     if pokemon in self.pokemons:
    #         return f"This pokemon is already caught"
    #     self.pokemons.append(pokemon)
    #     return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}' + '\n' + f'Pokemon count {len(self.pokemons)}'
        for x in self.pokemons:
            result += '\n'
            result += f'- {x.pokemon_details()}'

        return result

    # result = ""
    # result += f"Pokemon Trainer {self.name}" + "\n"
    #
    # result += f"Pokemon count {len(self.pokemons)}" + "\n"
    # for pok in self.pokemons:
    #     result += f"- {pok.pokemon_details()}"
    # return result
