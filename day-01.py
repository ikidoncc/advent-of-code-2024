def day_01():
    with open("./day-01.input.txt", "r") as file:
        s_input = file.read()

    column1 = []
    column2 = []

    for line in s_input.strip().split('\n'):
        values = line.split()
        column1.append(int(values[0]))
        column2.append(int(values[1]))

    column1.sort()
    column2.sort()

    total_distance = 0

    for index in range(len(column1)):
        total_distance += abs(column1[index] - column2[index])

    print("Result: ", total_distance)

day_01()