import re

total: int = 0
list_nums: list[int] = []
f = open("d1-input.txt", "r")

# Loop through each line in the file
for line in f:
    list_nums = []
    # Finds all the numbers and outputs list of ints with the all nums in the line
    for char in line:
        if char.isdigit():
            list_nums.append(int(char))
    line_total: int = int(f"{list_nums[0]}{list_nums[-1]}")
    total += line_total
print(total)
