# Part 2
def is_digit_letter(letters):
    if letters == "one":
        list_nums.append(1)
    elif letters == "two":
        list_nums.append(2)
    elif letters == "three":
        list_nums.append(3)
    elif letters == "four":
        list_nums.append(4)
    elif letters == "five":
        list_nums.append(5)
    elif letters == "six":
        list_nums.append(6)
    elif letters == "seven":
        list_nums.append(7)
    elif letters == "eight":
        list_nums.append(8)
    elif letters == "nine":
        list_nums.append(9)


total: int = 0
list_nums: list[int] = []
digit_letters: str = ""

f = open("d1-input.txt", "r")

# Loop through each line in the file
for line in f:
    list_nums = []
    # Finds all the numbers and outputs list of ints with the all nums in the line
    for char in line:
        if char.isdigit():
            list_nums.append(int(char))
        else:
            digit_letters += char
            if len(digit_letters) >= 3:
                is_digit_letter(digit_letters)
    line_total: int = int(f"{list_nums[0]}{list_nums[-1]}")
    total += line_total
print(total)
