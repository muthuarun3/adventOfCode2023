numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9

}


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


def switch(line: str) -> str:
    """
    Replaces the spelled numbers by the actual number
    """
    result = ''
    for i in range(len(line)):
        for number in numbers.keys():
            if number in line[i:i + len(number)]:
                result += str(numbers[number])
            else:
                result += str(line[i])
    return result


def get_digits_from_line(line: str, part: int) -> list[str]:
    """
    Takes a string and returns a list of each integer digit within the string, in the same order.

    """
    digits = []
    if part == 2:
        line = switch(line)
        # for number in numbers.keys():
        #     line = line.replace(number, str(numbers[number]))
    for character in line:
        if character.isnumeric():
            digits.append(character)
    return digits


def get_calibration_values_from_lines(lines: list[str], part: int) -> list[str]:
    """
    takes a list of lines and returns the associated list of calibration values
    """
    calibration_values = []
    for line in lines:
        calibration_value = None
        digits = get_digits_from_line(
            line=line,
            part=part
        )
        if len(digits) > 0:
            calibration_value = digits[0] + digits[-1]
        calibration_values.append(calibration_value)
    return calibration_values


def get_sum_of_calibration_values(calibration_values: list[str]) -> int:
    """
    Takes a list of string calibration values and returns the sum of all associated integers.
    """
    sum_of_calibration_values = 0
    for calibration_value in calibration_values:
        if calibration_value is not None:
            sum_of_calibration_values += int(calibration_value)
    return sum_of_calibration_values


def get_sum_from_file(file_path: str, part: int) -> int:
    """
    Takes the link to source txt file and returns
    """
    lines = get_lines_from_file(
        file_path=file_path
    )
    calibration_values = get_calibration_values_from_lines(
        lines=lines,
        part=part
    )
    sum_of_calibration_values = get_sum_of_calibration_values(
        calibration_values=calibration_values
    )
    return sum_of_calibration_values


def part_one():
    file_path = '../../resources/Day1/input.txt'
    answer1 = get_sum_from_file(
        file_path=file_path,
        part=1
    )
    print(f'For the first part, the sum of calibration values is : {answer1}')


def part_two():
    file_path = '../../resources/Day1/input.txt'
    answer2 = get_sum_from_file(
        file_path=file_path,
        part=2
    )
    print(f'For the second part, the sum of calibration values is : {answer2}')


if __name__ == '__main__':
    part_one()
    part_two()
