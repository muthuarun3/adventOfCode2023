from typing import Dict, List, Any


def get_lines_from_file(file_path: str) -> list[str]:
    """
    Takes the link from input file, and returns a list of strings, one for each line
    """
    with open(file_path, 'r') as file:
        raw_lines = file.readlines()
        lines = []
        for line in raw_lines:
            line = line.removesuffix('\n')
            lines.append(line)
    return lines


def get_numbers_map(lines: list[str]) -> list[list[int]]:
    map = []
    columns = range(len(lines[0]))
    for line in lines:
        map_line = []
        for column in columns:
            if line[column].isnumeric():
                map_line.append(1)
            else:
                map_line.append(0)
        map.append(map_line)
    return map


def get_numbers_in_map(numbers_map: list[list[int]], lines: list[str]) -> list[dict]:
    rows = len(numbers_map)
    columns = len(numbers_map[0])
    numbers = []
    for row in range(rows):
        i = 0
        while i < columns:
            if numbers_map[row][i] == 1:
                j = 0
                while numbers_map[row][i + j] == 1 and i + j < columns:
                    j += 1
                    if i + j >= columns:
                        break
                numbers.append(
                    {
                        "id": int(lines[row][i:i + j]),
                        "row": row,
                        "column_start": i,
                        "len": j,
                        "column_end": i + j - 1
                    }
                )
                i += j
            else:
                i += 1
    return numbers


def get_neighborhood(symbols_map: list[list[int]], numbers: list[dict]) -> list[dict]:
    last_row = len(symbols_map) - 1
    last_column = len(symbols_map[0]) - 1
    for number in numbers:
        symbols_top_row = []
        symbols_top_left = []
        symbols_top_right = []
        symbols_left = []
        symbols_right = []
        symbols_bottom_row = []
        symbols_bottom_left = []
        symbols_bottom_right = []

        row = number["row"]
        column_start = number["column_start"]
        column_end = number["column_end"]
        if row > 0:
            symbols_top_row = symbols_map[row - 1][column_start:column_end + 1]
            if column_start > 0:
                symbols_top_left = [symbols_map[row - 1][column_start - 1]]
            if column_end < last_column:
                symbols_top_right = [symbols_map[row - 1][column_end + 1]]
        else:
            pass
        if row < last_row:
            symbols_bottom_row = symbols_map[row + 1][column_start:column_end + 1]
            if column_start > 0:
                symbols_bottom_left = [symbols_map[row + 1][column_start - 1]]
            if column_end < last_column:
                symbols_bottom_right = [symbols_map[row + 1][column_end + 1]]
        if column_start > 0:
            symbols_left = [symbols_map[row][column_start - 1]]
        if column_end < last_column:
            symbols_right = [symbols_map[row][column_end + 1]]

        neighborhood = (
                symbols_top_left +
                symbols_top_row +
                symbols_top_right +

                symbols_left +
                symbols_right +

                symbols_bottom_left +
                symbols_bottom_row +
                symbols_bottom_right
        )
        number["neighborhood"] = neighborhood
    return numbers


def get_symbols_map(lines: list[str]) -> list[list[int]]:
    map = []
    columns = range(len(lines[0]))
    for line in lines:
        map_line = []
        for column in columns:
            if not (line[column].isnumeric() or line[column] == '.'):
                map_line.append(1)
            else:
                map_line.append(0)
        map.append(map_line)
    return map


def get_gear_map(lines: list[str]) -> list[list[int]]:
    """

    :rtype: object
    """
    map = []
    columns = range(len(lines[0]))
    gear_id = 1
    for line in lines:
        map_line = []
        for column in columns:
            if line[column] == "*":
                map_line.append(gear_id)
                gear_id += 1
            else:
                map_line.append(0)
        map.append(map_line)
    return map


def get_number_of_gears(gears_map: list[dict]) -> int:
    number_of_gears = 0
    for gear_line in gears_map:
        if max(gear_line) > number_of_gears:
            number_of_gears = max(gear_line)
    return number_of_gears


def get_gears(gear_numbers: list[dict]) -> list[dict]:
    numbers = []
    for gear_number in gear_numbers:
        gear = max(gear_number["neighborhood"])
        if gear != 0:
            gear_number["gear"] = gear
            numbers.append(gear_number)
        else:
            gear_number["gear"] = None

    return numbers
def get_gears_number(gear_numbers, number_of_gears):
    gear_dict = {}
    for i in range(number_of_gears):
        gn = []
        for gear_number in gear_numbers:
            if gear_number["gear"] == i + 1:
                gn.append(gear_number)
        if len(gn) > 1:
            gear_dict[i] = [g["id"] for g in gn]
    return gear_dict

def get_map_part_numbers(numbers: list[dict]) -> list[dict]:
    part_numbers = []
    for number in numbers:
        if 1 in number["neighborhood"]:
            part_numbers.append(number)
    return part_numbers

def get_sum_of_gears(gear_dict):
    s = 0
    for gears in gear_dict:
        m = 1
        for gear in gear_dict[gears]:
            m *= gear
        s += m
    return s
def get_sum_of_part_numbers(numbers: list[list[int]]) -> int:
    s = 0
    for number in numbers:
        s += number['id']
    return s


def part_one():
    file_path = '../../resources/Day3/input.txt'
    lines = get_lines_from_file(file_path)
    numbers_map = get_numbers_map(lines)
    symbols_map = get_symbols_map(lines)
    numbers = get_numbers_in_map(numbers_map, lines)
    numbers = get_neighborhood(symbols_map, numbers)
    part_numbers = get_map_part_numbers(numbers)
    s = get_sum_of_part_numbers(part_numbers)
    print(f'For the first part, the sum of part numbers is: {s}')


def part_two():
    file_path = '../../resources/Day2/input.txt'
    lines = get_lines_from_file(file_path)
    numbers_map = get_numbers_map(lines)
    numbers = get_numbers_in_map(numbers_map, lines)
    gears_map = get_gear_map(lines)
    number_of_gears = get_number_of_gears(gears_map)
    gear_numbers = get_neighborhood(gears_map, numbers)
    gear_numbers = get_gears(gear_numbers)
    gear_dict = get_gears_number(gear_numbers, number_of_gears)
    s = get_sum_of_gears(gear_dict)
    print(f'For the second part, the sum of gears is: {s}')


if __name__ == '__main__':
    file_path = '../../resources/Day3/input.txt'
    lines = get_lines_from_file(file_path)
    example = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..'
    ]
    parameter = example
    numbers_map = get_numbers_map(parameter)
    numbers = get_numbers_in_map(numbers_map, parameter)
    gears_map = get_gear_map(parameter)
    number_of_gears = get_number_of_gears(gears_map)
    gear_numbers = get_neighborhood(gears_map, numbers)
    gear_numbers = get_gears(gear_numbers)
    gear_dict = get_gears_number(gear_numbers, number_of_gears)
    s = get_sum_of_gears(gear_dict)
    print(s)

