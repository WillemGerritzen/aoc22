with open("input.txt", "r") as file:
    data = file.read().splitlines()


def compute_priority(string):
    mid_point = len(string) // 2
    fir_half, sec_half = set(string[:mid_point]), set(string[mid_point:])

    char_ascii = ord(str(fir_half.intersection(sec_half))[2])

    if 65 <= char_ascii <= 90:
        return char_ascii - 38

    return char_ascii - 96


print(sum([compute_priority(line) for line in data]))








