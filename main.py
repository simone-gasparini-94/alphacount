from stats import (
    convert_dict_to_list,
    get_num_of_chars,
    get_num_of_words,
    print_stats,
)


def get_book_text(path):
    with open(path, encoding="utf-8-sig") as file:
        return file.read()


def main():
    frankenstein_path = "books/frankenstein.txt"
    text = get_book_text(frankenstein_path)
    num_words = get_num_of_words(text)
    num_chars = get_num_of_chars(text)
    list = convert_dict_to_list(num_chars)
    print_stats(frankenstein_path, num_words, list)


main()
