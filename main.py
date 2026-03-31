def get_book_text(path):
    with open(path) as file:
        return file.read()


def get_num_of_words(string):
    return len(string.split())


def main():
    frankenstein_path = "./books/frankenstein.txt"
    num_words = get_num_of_words(get_book_text(frankenstein_path))
    print(f"Found {num_words} total words")


main()
