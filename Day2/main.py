# Advent of Code 2022 - day 2 part 1 and 2


# with open("input_test.txt", "r") as input_file:
def calculate_score(opponent_play, my_play):
    # Scores for the shapes
    shape_score = {"X": 1, "Y": 2, "Z": 3}

    # Scenarios to determine the outcome of the round
    win = [("A", "Y"), ("B", "Z"), ("C", "X")]
    draw = [("A", "X"), ("B", "Y"), ("C", "Z")]

    if (opponent_play, my_play) in win:
        outcome_score = 6
    elif (opponent_play, my_play) in draw:
        outcome_score = 3
    else:
        outcome_score = 0

    return shape_score[my_play] + outcome_score


def calculate_total_score(filename):
    total_score = 0

    with open(filename, "r") as file:
        for line in file:
            opponent_play, my_play = line.strip().split()
            total_score += calculate_score(opponent_play, my_play)

    return total_score


print(calculate_total_score("input_test.txt"))


# Advent of Code 2022 - day 2 part 2 and 2

# # Reading the input from file
# with open("input_test.txt", "r") as f:
#     rounds = [line.strip().split() for line in f.readlines()]

# # Scoring system
# scores = {"A": 1, "B": 2, "C": 3, "Win": 6, "Draw": 3, "Lose": 0}


# def play(opponent, outcome):
#     if opponent == "A":
#         if outcome == "Z":
#             return "B"
#         elif outcome == "Y":
#             return "A"
#         elif outcome == "X":
#             return "C"
#     elif opponent == "B":
#         if outcome == "Z":
#             return "C"
#         elif outcome == "Y":
#             return "B"
#         elif outcome == "X":
#             return "A"
#     elif opponent == "C":
#         if outcome == "Z":
#             return "A"
#         elif outcome == "Y":
#             return "C"
#         elif outcome == "X":
#             return "B"


# def get_outcome_score(opponent, shape):
#     if opponent == shape:
#         return "Draw"
#     elif (
#         (opponent == "A" and shape == "B")
#         or (opponent == "B" and shape == "C")
#         or (opponent == "C" and shape == "A")
#     ):
#         return "Win"
#     else:
#         return "Lose"


# total_score = 0
# for round in rounds:
#     opponent, outcome = round
#     shape = play(opponent, outcome)
#     result = get_outcome_score(opponent, shape)
#     total_score += scores[shape] + scores[result]

# print(total_score)

# Reading the input from file
with open("input_test.txt", "r") as f:
    rounds = [line.strip().split() for line in f.readlines()]

# Scoring system
shape_scores = {"A": 1, "B": 2, "C": 3}
outcome_scores = {"Win": 6, "Draw": 3, "Lose": 0}

# Optimal shapes to choose given the opponent's shape and desired outcome
optimal_shapes = {
    "A": {"Z": "B", "Y": "A", "X": "C"},
    "B": {"Z": "C", "Y": "B", "X": "A"},
    "C": {"Z": "A", "Y": "C", "X": "B"},
}


def get_outcome(opponent, shape):
    if opponent == shape:
        return "Draw"
    elif (
        (opponent == "A" and shape == "B")
        or (opponent == "B" and shape == "C")
        or (opponent == "C" and shape == "A")
    ):
        return "Win"
    else:
        return "Lose"


total_score = 0
for opponent, desired_outcome in rounds:
    # Choose the optimal shape based on opponent's shape and desired outcome
    chosen_shape = optimal_shapes[opponent][desired_outcome]

    result = get_outcome(opponent, chosen_shape)

    total_score += shape_scores[chosen_shape] + outcome_scores[result]

print(total_score)
