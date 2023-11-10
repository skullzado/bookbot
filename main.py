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
