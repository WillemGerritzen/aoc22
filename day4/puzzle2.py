
with open('input.txt', 'r') as file:
    data = [x.split(',') for x in file.read().splitlines()]


def find_overlap(data):
    for pairs in data:
        pair11, pair12, pair21, pair22 = int(pairs[0].split('-')[0]), int(pairs[0].split('-')[1]), int(pairs[1].split('-')[0]), int(pairs[1].split('-')[1])
        yield (pair11 <= pair21 and pair12 >= pair22) or (pair21 <= pair11 and pair22 >= pair12)


if __name__ == "__main__":
    overlap = list(find_overlap(data))
    print(sum(overlap))
