import numpy as np

board = np.array([
    [7, 0, 0, 0, 3, 9, 0, 0, 4],
    [0, 0, 2, 0, 8, 0, 0, 0, 0],
    [0, 0, 0,4, 0, 1, 0, 0, 2],
    [9, 0, 1, 0, 0, 3, 0, 0, 0],
    [0, 2, 7, 5, 0, 8, 6, 3, 0],
    [0, 0, 0, 1, 0, 0, 9, 0, 7],
    [8, 0, 0, 9, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 5, 0, 0],
    [2, 0, 0, 3, 5, 0, 0, 0, 8],
])


def print_board(brd):
    for i in range(len(brd)):  # catch row
        if i % 3 == 0 and i != 0:
            print("----------------------")
        for j in range(len(brd[0])):  # catch column
            if j % 3 == 0 and j != 0:
                print(' |', end="")

            print(f" {brd[i][j]}", end="")
            if j == len(brd[0]) - 1:
                print()


def check_row_column(array, num):
    for i in array:
        if i == num:
            return True
    return False


def check_sub_group(pos, brd, num):
    for i in range(len(brd)):  # catch row
        if pos[0] // 3 == i // 3:
            for j in range(len(brd[0])):  # catch column
                if pos[1] // 3 == j // 3:
                    if num == brd[i][j]:
                        return True
    return False


def get_empty(brd):
    list = []
    for i in range(len(brd)):  # catch row
        for j in range(len(brd[0])):  # catch column
            if brd[i][j] == 0:
                list.append((i, j))
    return list


def main(brd):
    zeros = get_empty(brd)
    z = 0
    while z < len(zeros) and z>=0:
        num = brd[zeros[z]] + 1
        while num < 10:
            if not check_row_column(brd[zeros[z][0]], num) and not check_row_column(brd[:, zeros[z][1]],num) and not check_sub_group(zeros[z],brd,num):
                brd[zeros[z]] = num
                break
            else:
                num += 1
        if num>=10:
            brd[zeros[z]] =0
            z-=1
        else:
            z+=1
    print_board(brd)


if __name__ == '__main__':
    print("input puzzle")
    print_board(board)
    print("output")
    main(board)
    # print_board(board)
