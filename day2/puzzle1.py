import timeit

# Puzzle 1
score_table = {
    "X": dict(A=3, B=1, C=2),
    "Y": dict(A=4, B=5, C=6),
    "Z": dict(A=8, B=9, C=7),
}

# Puzzle 2
# score_table = {
#     "X": dict(A=3, B=1, C=2),
#     "Y": dict(A=4, B=5, C=6),
#     "Z": dict(A=8, B=9, C=7),
# }


def compute_score(opponent, player):
    return score_table[player][opponent]


def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    score_per_game = sum([compute_score(x, y) for x, _, y in data])

    print(score_per_game)


if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    execution_time = stop - start

    print("Program Executed in " + str(execution_time))
