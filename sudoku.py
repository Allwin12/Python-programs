grid = [
    [5, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 0, 0]
]


def find_empty_space():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def check_possible(row, column, value):
    for i in range(9):
        if grid[row][i] == value:
            return False
    for i in range(9):
        if grid[i][column] == value:
            return False

    small_x = (row // 3) * 3
    small_y = (column // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[small_x + i][small_y + j] == value:
                return False
    return True


def print_grid():
    print('___________________________________\n')
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=' | ')
        print('\n')
    print('___________________________________')


def solve():
    if not find_empty_space():
        return True

    row, column = find_empty_space()
    for number in range(1, 10):
        if check_possible(row, column, number):
            grid[row][column] = number

            if solve():
                return True
            grid[row][column] = 0
    return False


solve()
print_grid()
