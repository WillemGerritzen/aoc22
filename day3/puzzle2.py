with open("input.txt", "r") as file:
    data = file.read().splitlines()


def divide_into_groups(data_):
    for idx in range(0, len(data_), 3):

        yield data_[idx:idx + 3]


def find_common_letter(groups_):
    for group in groups_:

        yield set(group[0]).intersection(set(group[1]), set(group[2]))


def compute_priority(chars):
    for char in chars:

        char_ascii = ord(str(char)[2])

        if 65 <= char_ascii <= 90:
            yield char_ascii - 38

        else:
            yield char_ascii - 96


groups = list(divide_into_groups(data))
common_letters = list(find_common_letter(groups))
priorities = list(compute_priority(common_letters))
print(sum(priorities))









