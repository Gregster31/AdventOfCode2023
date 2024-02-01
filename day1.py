# Part 2
def is_digit_letter(letters):
    global digit_letters
    if letters == "one":
        list_nums.append(1)
        digit_letters = ""

    elif letters == "two":
        list_nums.append(2)
        digit_letters = ""

    elif letters == "three":
        list_nums.append(3)
        digit_letters = ""

    elif letters == "four":
        list_nums.append(4)
        digit_letters = ""

    elif letters == "five":
        list_nums.append(5)
        digit_letters = ""

    elif letters == "six":
        list_nums.append(6)
        digit_letters = ""

    elif letters == "seven":
        list_nums.append(7)
        digit_letters = ""

    elif letters == "eight":
        list_nums.append(8)
        digit_letters = ""

    elif letters == "nine":
        list_nums.append(9)
        digit_letters = ""


total: int = 0
list_nums: list[int] = []
digit_letters: str = ""

f = open("d1-input.txt", "r")

# Loop through each line in the file
for line in f:
    list_nums = []
    digit_letters: str = ""
    # Finds the first int in array --> Starts to search backwards
    for char in line:
        # Char is int
        if char.isdigit():
            list_nums.append(int(char))
            for rchar in reversed(line):
                if rchar.isdigit():
                    list_nums.append(int(rchar))
                    break
                else:
                    digit_letters += rchar
                    if len(digit_letters) >= 3:
                        is_digit_letter(reversed(digit_letters))
        # Char is letter
        else:
            digit_letters += char
            if len(digit_letters) >= 3:
                is_digit_letter(digit_letters)

    line_total: int = int(f"{list_nums[0]}{list_nums[-1]}")
    total += line_total
print(total)