from typing import Dict, List, Any

bag = dict(red=12, blue=14, green=13)


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


class Game:
    def __init__(self):
        self.sets = None
        self.index = 0

    def set_from_string(self, input_string: str):
        game = input_string.split(':')
        self.index = int(game[0].removeprefix('Game '))
        raw_sets = game[1].split(';')
        clean_sets = []
        for raw_set in raw_sets:
            clean_set = raw_set.split(',')
            dict_set = dict()
            for elem in clean_set:
                draw = elem.split(' ')
                dict_set[draw[2]] = int(draw[1])
                clean_sets.append(dict_set)
        self.sets = clean_sets

    @property
    def drawn_cubes(self):
        cubes: dict[str, list[Any]] = dict(red=[], blue=[], green=[])
        for game_set in self.sets:
            for color in game_set.keys():
                cubes[color].append(game_set[color])
        return cubes

    @property
    def cubes(self):
        cubes: dict[str, int] = dict(red=0, blue=0, green=0)
        for color in self.drawn_cubes.keys():
            cubes[color] = sum(self.drawn_cubes[color])
        return cubes

    @property
    def possible(self):
        game_possible = True
        for game_set in self.sets:
            for color in game_set.keys():
                if game_set[color] > bag[color]:
                    game_possible = False
        return game_possible

    @property
    def fewest_cubes(self):
        cubes: dict[str, int] = dict(red=0, blue=0, green=0)
        for color in self.drawn_cubes.keys():
            cubes[color] = max(self.drawn_cubes[color])
        return cubes

    @property
    def power(self):
        power = 1
        for color in self.fewest_cubes.keys():
            power = power * self.fewest_cubes[color]
        return power


def part_one():
    file_path = '../../resources/Day2/input.txt'
    lines = get_lines_from_file(file_path)
    possible_games = []
    for line in lines:
        game = Game()
        game.set_from_string(line)
        if game.possible:
            possible_games.append(game.index)
    print(f'For the first part, the sum of ids of possible games is: {sum(possible_games)}')


def part_two():
    file_path = '../../resources/Day2/input.txt'
    lines = get_lines_from_file(file_path)
    total_power = 0
    for line in lines:
        game = Game()
        game.set_from_string(line)
        total_power += game.power
    print(f'For the second part, the sum of powers for each game is: {total_power}')


if __name__ == '__main__':
    part_one()
    part_two()