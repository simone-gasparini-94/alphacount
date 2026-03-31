from stats import get_num_of_words


def get_book_text(path):
    with open(path) as file:
        return file.read()


def main():
    frankenstein_path = "./books/frankenstein.txt"
    num_words = get_num_of_words(get_book_text(frankenstein_path))
    print(f"Found {num_words} total words")


main()
