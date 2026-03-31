def sort_list_by_value(list_of_dict):
    for i in range(0, len(list_of_dict)):
        for j in range(1, len(list_of_dict) - i):
            prev = list(list_of_dict[j - 1].values())[0]
            curr = list(list_of_dict[j].values())[0]
            if prev > curr:
                tmp = list_of_dict[j - 1]
                list_of_dict[j - 1] = list_of_dict[j]
                list_of_dict[j] = tmp


def main():
    list = []
    list.append({"a": 3})
    list.append({"b": 5})
    list.append({"c": 4})

    sort_list_by_value(list)
    print(list)


main()
