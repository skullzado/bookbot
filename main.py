with open("books/frankenstein.txt") as f:
    file_contents = f.read()


# Count all words
def count_words(text):
    return len(text.split())


