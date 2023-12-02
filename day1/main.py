# 1. two pointer
mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_number(text):
    first_digit = None
    last_digit = None
    for char in text:
        if char.isdigit():
            first_digit = int(char)
            break

    for char in reversed(text):
        if char.isdigit():
            last_digit = int(char)
            break
    return first_digit * 10 + last_digit


def get_number2(text):
    buffer = ""
    first_digit = None
    last_digit = None
    for char in text:
        if char.isdigit():
            first_digit = int(char)
            break
        else:
            buffer += char
            valid_substring = [
                substring for substring in mapping.keys() if substring in buffer
            ]
            if valid_substring:
                first_digit = mapping[valid_substring[0]]
                break
    buffer = ""
    for char in reversed(text):
        if char.isdigit():
            last_digit = int(char)
            break
        else:
            buffer = char + buffer
            valid_substring = [
                substring for substring in mapping.keys() if substring in buffer
            ]
            if valid_substring:
                last_digit = mapping[valid_substring[0]]
                break
    return first_digit * 10 + last_digit


with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f]
    total_part1 = 0
    total_part2 = 0
    for line in lines:
        total_part1 += get_number(line)
        total_part2 += get_number2(line)

    print("part 1 ans:", total_part1)
    print("part 2 ans", total_part2)
