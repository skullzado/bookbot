with open("books/frankenstein.txt") as f:
    file_contents = f.read()


# Count all words
def count_words(text):
    return len(text.split())


# Count all letters
def count_letters(text):
    letter_count = {}
    text = text.lower()
    for char in text:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count


# Print a report
def print_a_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document\n")

    letter_count = list(count_letters(text).items())
    letter_count.sort()
    for item in letter_count:
        if item[0].isalpha():
            print(
                f"The '{item[0]}' character was found {item[1]} times")

    print("\n--- End report ---")
