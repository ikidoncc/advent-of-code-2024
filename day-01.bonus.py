def day_01_bonus():
    with open("./day-01.bonus.input.txt", "r") as file:
        s_input = file.read()
    
    column1 = []
    column2 = []

    for line in s_input.strip().split('\n'):
        values = line.split()
        column1.append(int(values[0]))
        column2.append(int(values[1]))

    total_score = 0

    for number in column1:
        total_score += number * column2.count(number)

    print(total_score)

day_01_bonus()