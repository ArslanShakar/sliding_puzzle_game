def check_win(puzzle: str, solution: str) -> bool:
    for i, s in enumerate(puzzle):
        if s == ' ':
            s = solution[i]
            puzzle = puzzle.replace(' ', s)
        if s != solution[i]:
            return False
    return True


print(check_win("abcdefgh ", "abcdefghi"))
print(check_win("dabecghf ", "abcdefghi"))


def swap_position(puzzle: str, from_index: int, to_index: int) -> str:
    from_char = puzzle[from_index]

    chars = list(puzzle)
    chars[from_index] = chars[to_index]
    chars[to_index] = from_char
    puzzle = ''.join(chars)
    print(puzzle)
    return puzzle

# def swap_position(puzzle: str, from_index: int, to_index: int) -> str:
#     chars = list(puzzle)
#     chars[from_index], chars[to_index] = chars[to_index], puzzle[from_index]
#     puzzle = ''.join(chars)
#     print(puzzle)
#     return puzzle


swap_position("care", 0, 2)
swap_position("does", 3, 2)
