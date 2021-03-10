grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 0, 0]
]


def check_possible(row, column, value):
    global grid
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
    global grid
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=' | ')
        print('\n')


def solve():
    global grid
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                for number in range(1, 10):
                    if check_possible(i, j, number):
                        grid[i][j] = number
                        solve()
                        grid[i][j] = 0
                return


solve()
print_grid()
