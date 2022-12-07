with open('input.txt', 'r') as file:
    data = file.readlines()
    moves = [list(x.replace('move', '').replace('from', '').replace('to', '').lstrip().rstrip().replace(' ', '')) for x in data[data.index('\n') + 1:]]
    rows = [int(x) for x in data[data.index('\n') - 1].split()]
    pre_crates = [list(x.replace('[', '').replace(']', '').replace('    ', '0').replace(' ', '').replace('\n', '0')[:len(rows)]) for x in data[:data.index('\n') - 1]]

    for crates in pre_crates:
        while len(crates) != len(rows):
            crates.append('0')

    crates = {y + 1: list(x)[::-1] for y, x in enumerate(zip(*pre_crates))}
    for crate in crates.values():
        while '0' in crate:
            crate.remove('0')

for move in moves:
    to = int(move.pop())
    from_ = int(move.pop())
    count = int(''.join([x for x in move]))
    crates_to_move = []
    for round_ in range(count):
        crates_to_move.append(crates[from_].pop())
    crates_to_move.reverse()
    crates[to].extend(crates_to_move)


print(''.join([c[-1] for c in crates.values()]))
