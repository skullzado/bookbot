import sys
from stats import count_words,  count_characters, char_list

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def book_report(word_count: int, list_of_char: list, filepath: str) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    for i in range(len(list_of_char)):
        print(f"{list_of_char[i]["char"]}: {list_of_char[i]["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    word_count = count_words(file_contents)
    char_count_dict = count_characters(file_contents)
    list_of_char = char_list(char_count_dict)
    book_report(word_count, list_of_char, filepath)


main()