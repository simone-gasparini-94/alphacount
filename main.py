from stats import get_num_of_chars, get_num_of_words


def get_book_text(path):
    with open(path, encoding="utf-8-sig") as file:
        return file.read()


def main():
    frankenstein_path = "./books/frankenstein.txt"
    text = get_book_text(frankenstein_path)
    num_words = get_num_of_words(text)
    print(f"Found {num_words} total words")
    num_chars = get_num_of_chars(text)
    print(num_chars)


main()
