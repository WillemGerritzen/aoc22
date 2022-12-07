with open('input.txt', 'r') as file:
    data = file.read().splitlines()


def find_marker(string):
    for count, char in enumerate(string[3:]):
        substring = string[count: count + 4]
        if len(set(substring)) == 4:
            return count + 4


for string in data:
    print(find_marker(string))
