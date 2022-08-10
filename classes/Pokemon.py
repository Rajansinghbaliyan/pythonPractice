import textwrap


class Pokemon:
    def __init__(self, name, weight, height, base_experience, id):
        self.name = name
        self.weight = weight
        self.height = height
        self.base_experience = base_experience
        self.id = id

    def factory(pokemon_json):
        return Pokemon(
            pokemon_json['name'],
            pokemon_json['weight'],
            pokemon_json['height'],
            pokemon_json['base_experience'],
            pokemon_json['id']
        )

    def __str__(self) -> str:
        return textwrap.dedent(f'''
        Pokemon:-
        name: {self.name}
        weight: {self.weight}
        height: {self.height}
        base_experience: {self.base_experience}
        id: {self.id}
        ''')


Pokemon.factory = staticmethod(Pokemon.factory)
