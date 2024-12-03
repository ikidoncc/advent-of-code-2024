# Rules:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.

def formatter(file):
    return file.readline().strip()

def is_valid_sequence(levels):
    levels = list(map(int, levels))

    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    is_valid_difference = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
    
    return (is_increasing or is_decreasing) and is_valid_difference

def day_02():
    with open("./day-02.input.txt", "r") as file:
        reports = []
        line = formatter(file)

        while line:
            reports.append(line.split(' '))
            line = formatter(file)

    total_levels_valid = 0

    for level in reports:
        if is_valid_sequence(level):
            total_levels_valid += 1
    
    print(total_levels_valid)

day_02()
