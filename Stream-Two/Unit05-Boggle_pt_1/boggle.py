from string import ascii_uppercase
from random import choice


def check():
    return 1


def make_grid(width, height):
    return {(row, col): choice(ascii_uppercase)
            for row in range(height)
            for col in range(width)}


def neighbours_of_position((row, col)):
    return [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1),                     (row, col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]


def all_grid_neighbours(grid):
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours


def path_to_word(grid, path):
    return ''.join([grid[p] for p in path])


def search(grid, dictionary):
    neighbours = all_grid_neighbours(grid)
    paths = []

    def do_search(path):
        word = path_to_word(grid, path)
        if word in dictionary:
            paths.append(path)
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])

    for position in grid:
        do_search([position])

    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)


def get_dictionary(dictionary_file):
    with open(dictionary_file) as f:
        return [w.strip().upper() for w in f]


def main():
    grid = make_grid(3, 3)
    dictionary = get_dictionary('words.txt')
    words = search(grid, dictionary)
    for word in words:
        print word
    print "Found {0} words".format(len(words))

main()