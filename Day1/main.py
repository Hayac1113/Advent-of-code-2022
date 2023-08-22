# Advent of Code 2022 - day 1 part 1 and 2


# Add values together until you see an empty line
# if you see an empty line start counting again

# /n

# Problem 1: recognize the empty line
# Solution 1: A empty line is equal to the empty string (after .strip())

# Open the input file for reading
with open("input_test.txt", "r") as input_file:
    elves_calories = []  # List to store total calories for each elf
    current_value = 0

    for line in input_file:
        stripped = line.strip()

        # If the line is not empty, add its value to current_value
        if stripped != "":
            current_value += int(stripped)

        # If the line is empty, it means we're moving to the next elf. Store current_value and reset it.
        else:
            elves_calories.append(current_value)
            current_value = 0

    # Make sure to add the last elf's calories if the file doesn't end with an empty line
    if current_value != 0:
        elves_calories.append(current_value)

    # Sort the list in descending order and get the sum of the top three values
    elves_calories.sort(reverse=True)
    top_three_total = sum(elves_calories[:3])

    print(f"Elf with most calories: {elves_calories[0]}")
    print(f"Top three elves' total calories: {top_three_total}")
