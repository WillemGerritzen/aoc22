with open('input.txt', 'r') as file:
    data = file.read().splitlines()


def find_marker(string):
    for count, char in enumerate(string[13:]):
        substring = string[count: count + 14]
        if len(set(substring)) == 14:
            return count + 14


for string in data:
    print(find_marker(string))
