from helpers import read_data

def day_2_1():

    cubes = {"red": 12, "green": 13, "blue": 14}

    data = read_data("2")
    possible_rounds = []

    for row in data.split("\n"):
        id = row.split(" ")[1][:-1]
        possible = True

        game_data = row.split(": ")[1].split(";")
        for round in game_data:
            for boxes in round.split(","):
                round_boxes = boxes.strip().split(" ")
                if int(round_boxes[0]) > cubes[round_boxes[1]]:
                    possible = False
        if possible == True:
            possible_rounds.append(int(id))
        
    return sum(possible_rounds)

def day_2_2():

    data = read_data("2")

    final_result = 0 
    for row in data.split("\n"):
        game_values = {"red": 0, "green": 0, "blue": 0}
        game_data = row.split(": ")[1].split(";")
        for round in game_data:
            for boxes in round.split(","):
                colour = boxes.strip().split(" ")[1]
                qty = int(boxes.strip().split(" ")[0])
                if qty > game_values[colour]:
                    game_values[colour] = qty 
        final_result += (game_values["red"] * game_values["green"] * game_values["blue"])

    return final_result

print(f"Solution for Day 2.1: {day_2_1()}")
print(f"Solution for Day 2.2: {day_2_2()}")