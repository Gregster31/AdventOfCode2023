import re

total: int = 0
f = open("d1-input.txt", "r")

# Loop through each line in the file
for line in f:
    # Finds all the numbers and outputs list of ints with the all nums in the line
    # todo because all the nums are one after the other it fucks up and takes all the nums
    list_nums_in_current_line = list(map(int, re.findall("\d+", line)))
    # Puts the two int nums together
    line_num: int = int(f"{list_nums_in_current_line[0]}{list_nums_in_current_line[-1]}")
    total += line_num
print(total)
print("hello")
