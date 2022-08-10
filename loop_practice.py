from classes.Pokemon import Pokemon
from classes.PokemonApi import PokemonApi


def loop_call_method():
    print('loops')
    get_pokemon()


def get_pokemon():
    pokemon_json = PokemonApi().get_pokemon_by_id(1)
    pokemon = Pokemon.factory(pokemon_json)
    print(pokemon)
    return pokemon
