"""
Sliding Puzzle Game
Assignment 1
Semester 1, 2021
CSSE1001/CSSE7030
"""

from a1_support import *


# Replace these <strings> with your name, student number and email address.
__author__ = "<Your Name>, <Your Student Number>"
__email__ = "<Your Student Email>"


def shuffle_puzzle(solution: str) -> str:
    """
    Shuffle a puzzle solution to produce a solvable sliding puzzle.

    Parameters:
        solution (str): a solution to be converted into a shuffled puzzle.

    Returns:
        (str): a solvable shuffled game with an empty tile at the
               bottom right corner.

    References:
        - https://en.wikipedia.org/wiki/15_puzzle#Solvability
        - https://www.youtube.com/watch?v=YI1WqYKHi78&ab_channel=Numberphile

    Note: This function uses the swap_position function that you have to
          implement on your own. Use this function when the swap_position
          function is ready
    """
    shuffled_solution = solution[:-1]

    # Do more shuffling for bigger puzzles.
    swaps = len(solution) * 2
    for _ in range(swaps):
        # Pick two indices in the puzzle randomly.
        index1, index2 = random.sample(range(len(shuffled_solution)), k=2)
        shuffled_solution = swap_position(shuffled_solution, index1, index2)

    return shuffled_solution + EMPTY


def check_win(puzzle: str, solution: str) -> bool:
    for i, s in enumerate(puzzle):
        if s == ' ':
            s = solution[i]
            puzzle = puzzle.replace(' ', s)
        if s != solution[i]:
            return False
    return True


def swap_position(puzzle: str, from_index: int, to_index: int) -> str:
    chars = list(puzzle)
    chars[from_index], chars[to_index] = chars[to_index], puzzle[from_index]
    puzzle = ''.join(chars)
    return puzzle


def move(puzzle: str, direction: str):
    from_index, to_index = None, puzzle.find(' ')

    try:
        if direction == UP:
            from_index = to_index - difficulty_level
            out_range = [0, difficulty_level - 1]
            if to_index in out_range:
                print(INVALID_MOVE_FORMAT.format(to_index))
                return
            puzzle = swap_position(puzzle, to_index, from_index)
        elif direction == DOWN:
            from_index = to_index + difficulty_level
            out_range = [
                difficulty_level * (difficulty_level - 1),
                difficulty_level*difficulty_level - 1,
            ]

            if to_index in out_range:
                print(INVALID_MOVE_FORMAT.format((to_index)))
                return
            puzzle = swap_position(puzzle, from_index, to_index)
        elif direction == LEFT:
            from_index = to_index - 1
            if to_index in [difficulty_level * e for e in range(difficulty_level)]:
                print(INVALID_MOVE_FORMAT.format((to_index)))
                return
            puzzle = swap_position(puzzle, from_index, to_index)
        elif direction == RIGHT:
            from_index = to_index + 1
            out_range = [difficulty_level * e for e in range(1, difficulty_level + 1)]

            if from_index in out_range:
                print(INVALID_MOVE_FORMAT.format((from_index)))
                return

            # if to_index < difficulty_level and to_index <= len(puzzle):
            puzzle = swap_position(puzzle, from_index, to_index)
        elif direction == HELP:
            print(HELP_MESSAGE)
        else:
            print(INVALID_MESSAGE)

    except Exception as err:
        print(INVALID_MOVE_FORMAT.format((to_index, from_index)))

    return puzzle


def print_grid(puzzle):
    puzzle_chars = list(puzzle)

    row = CORNER + f"{EMPTY}{HORIZONTAL_WALL}{EMPTY}{CORNER}" * difficulty_level
    print(row)

    for row_i in range(difficulty_level):
        r = f"{VERTICAL_WALL}".join(f"{EMPTY}{puzzle_chars.pop(0)}{EMPTY}" for _ in range(difficulty_level))
        print(f"{VERTICAL_WALL}{r}{VERTICAL_WALL}")
        print(row)


# print_grid(3, 8)

def main():
    """Entry point to gameplay"""

    print(WELCOME_MESSAGE)
    global difficulty_level
    difficulty_level = input(BOARD_SIZE_PROMPT)
    is_difficulty_level_valid = all([d.isdigit() for d in difficulty_level])

    if not difficulty_level.strip() or not is_difficulty_level_valid:
        print(INVALID_MESSAGE)
        exit()

    # Type Casting: str to int
    difficulty_level = int(difficulty_level)

    # Call Function: get_game_solution
    solution = get_game_solution(WORDS_FILE, difficulty_level)

    # Call Function: shuffle_puzzle
    puzzle = shuffle_puzzle(solution)

    while True:
        print("Solution:")
        print_grid(solution)

        print("\nCurrent position:")
        print_grid(puzzle)

        direction = input('\n' + DIRECTION_PROMPT).strip().upper()
        if direction == GIVE_UP:
            print(GIVE_UP_MESSAGE)
            break

        moved = move(puzzle, direction)
        if not moved:
            continue

        if check_win(puzzle, solution):
            print(WIN_MESSAGE)
            break
        puzzle = moved

    if input(PLAY_AGAIN_PROMPT).strip().upper() == 'Y':
        main()
        return

    print(BYE)


if __name__ == "__main__":
    main()
