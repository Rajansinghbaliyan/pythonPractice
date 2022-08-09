def call_string_functions(string, index):
    uses_of_index(string, index)
    practicing_with_string_sequence(string)
    reverse_only_words("Hello World")


def uses_of_index(string, index):
    first_character = get_character_by_index(string, index)
    print(f'first character is {first_character}')


def get_character_by_index(string, index):
    if index > len(string):
        print(f"Index should be less than the {len(string)}")
        return
    try:
        character = string[index]
        return character
    except IndexError as err:
        print(f'An error occurred: {err}')
        return


def practicing_with_string_sequence(string):
    last_4_character = string[-4:]
    print_result(string, "The last four character", last_4_character)

    reversed_string = string[::-1]
    print_result(string, "reverse", str(reversed_string))

    # here only character upto index 3 is taken, 4 index in not included
    first_4_character = string[:4]
    print_result(string, "first four character", first_4_character)


def print_result(string, message, result):
    print(f'{message} of {string}: {result}')


def reverse_only_words(line):
    if isinstance(line, str):
        result = ""
        for string in split_string(line, " "):
            result = f'{string} {result}'
        print(result)
        return result
    else:
        print("Please enter string")


def split_string(string, sequence):
    return string.split(sequence)
