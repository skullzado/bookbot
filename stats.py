def count_words(file: str) -> int:
    word_count = len(file.split())
    
    return word_count


def count_characters(file: str) -> object:
    characters_found = {}

    for char in file:
        char_lower = char.lower()
        if char.lower() in characters_found:
            characters_found[char_lower] += 1
        else:
            characters_found[char_lower] = 1

    return characters_found


def sort_on(dict):
    return dict["num"]


def char_list(characters_dict: object) -> list:
    new_list = []

    for char in characters_dict:
        if char.isalpha():
            new_list.append({"char": char, "num": characters_dict[char]})

    new_list.sort(reverse=True, key=sort_on)

    return new_list