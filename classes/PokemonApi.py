from constants.pokemon_api import POKEMON_URL
from utils.fetch_data import get_data_from_url


class PokemonApi:
    def get_pokemon_by_id(pokemon_id):
        url = f'{POKEMON_URL}/{pokemon_id}'
        pokemon_json = get_data_from_url(url)
        return pokemon_json


PokemonApi.get_pokemon_by_id = staticmethod(PokemonApi.get_pokemon_by_id)
