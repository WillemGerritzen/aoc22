import timeit

with open("input.txt", "r") as input_file:
    start = timeit.default_timer()

    input_list = input_file.read().splitlines()
    idx_newline = [i for i, x in enumerate(input_list) if x == '']
    nested_list = [list(map(int, input_list[i + 1 if i != 0 else i:j])) for i, j in zip([0] + idx_newline, idx_newline)]
    print(max(sum(lst) for lst in nested_list))

    stop = timeit.default_timer()
    execution_time = stop - start

    print("Program Executed in " + str(execution_time))
