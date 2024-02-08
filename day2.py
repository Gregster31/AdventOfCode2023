# open puzzle input: d2-input.txt
def read_input(day_num):
    with open(f'd{day_num}-input.txt', 'r') as f:
        data = f.read().splitlines()
    return data

### PART 1 ###

# define a dictionary with the max cubes for each color
max_cubes = {
    'b': 14,
    'r': 12,
    'g': 13
}
def part1():
    sum_of_games: int = 0
    game_infos: str
    cubes_infos: str
    for i in read_input("2"):
        grabs: list[str] = []
        # Split1, splits the game num and cubes infos [Game 1] [3 red, 1 green; 2 blue, 1 red]
        game_infos, cubes_infos = i.split(": ")
        # Split2, splits the grabs [3 red, 1 green] [2 blue, 1 red]
        grabs = cubes_infos.split("; ")

        # Split3, splits the cube infos [3 red] [1 green]
        for x in grabs:
            different_colors: list[str] = x.split(", ")
            # Check for color, then check if num of cubes is under limit
            for y in different_colors:
                if y[2] in max_cubes:
                    # Check if num of cubes is lower than limit
                    if y[0] < max_cubes[y[2]]:
                        continue
                    else:
                        print("This game does not exist. Too many cubes grabbed!")
                else:
                    print("Color does not exist!")