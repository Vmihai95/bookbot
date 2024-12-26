def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    print("--- Begin report of books/frankenstein.txt  ---")
    print(f"{num_words} words found in the document")
    print()
    for char in sorted(char_count):
        print(f"The '{char}' character was found {char_count[char]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count




main()
