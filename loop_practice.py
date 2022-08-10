from classes.Pokemon import Pokemon
from classes.PokemonApi import PokemonApi
from constants.print_iterator import print_iter


def loop_call_method():
    print('loops')
    pokemon_dis = get_pokemon_between_range(1, 5)
    print_iter(pokemon_dis)


def get_pokemon_between_range(start, end):
    pokemon_dis = {}
    for id in range(start, end):
        pokemon = get_pokemon(id)
        pokemon_dis[pokemon.name] = pokemon
    return pokemon_dis


def get_pokemon(id):
    pokemon_json = PokemonApi().get_pokemon_by_id(id)
    pokemon = Pokemon.factory(pokemon_json)
    return pokemon
