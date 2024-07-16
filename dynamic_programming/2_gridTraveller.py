def grid(row, column, mem={}):
    key = str(row) + ',' + str(column)

    if row == 0 or column == 0:
        return 0
    if row == 1 and column == 1:
        return 1
    if key in mem:
        return mem[key]

    mem[key] = grid(row - 1, column, mem) + grid(row, column - 1, mem)

    return mem[key]


print(grid(3, 3))
