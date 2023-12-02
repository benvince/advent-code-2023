from helpers import read_data

def day_1_1() -> int:

    data = read_data("1")

    total = 0
    for row in data.split():
        row_value =  "".join([x for x in row if x.isnumeric()])
        total += int(row_value[0] + row_value[-1])

    return total

def day_1_2() -> int:


    numbers = {
        'one': "o1e",
        'two': "t2o",
        'three': "t3e",
        'four': "f4r",
        'five': "f5e",
        'six': "s6x",
        'seven': "s7n",
        'eight': "e8t",
        'nine': "n9e"
    }

    data = read_data("1")

    total = 0
    for row in data.split():
        for num in numbers:
            row = row.replace(num,numbers[num])
        row_value =  "".join([x for x in row if x.isnumeric()])
        total += int(row_value[0] + row_value[-1])

    return total



print(f"Day 1_1 Answer: {day_1_1()}")
print(f"Day 1_2 Answer: {day_1_2()}")