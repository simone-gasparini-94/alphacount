def get_num_of_words(string):
    return len(string.split())


def get_num_of_chars(string):
    chars = {}
    for char in string:
        lower_case = char.lower()
        if lower_case not in chars:
            chars[lower_case] = 1
            continue
        chars[lower_case] += 1
    return chars
