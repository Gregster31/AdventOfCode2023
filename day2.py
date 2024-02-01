# Day 2
f = open("d2-input.txt", "r")
# 12 red cubes, 13 green cubes, and 14 blue cubes?
MAX_RED: int = 12
MAX_BLUE:int = 14
MAX_GREEN:int = 13

# Game 2: 6 red, 11 green; 4 blue, 4 green, 5 red; 11 green, 6 blue, 6 red
for line in f:
    # Separate Game from cubes
    game_infos, cubes_infos = line.split(": ")
    cubes_rolled: int | str = cubes_infos.split(", |; ")
    num, color = cubes_rolled.split(" ")
    # Add the nums of cubes
    for x in len(cubes_rolled):










