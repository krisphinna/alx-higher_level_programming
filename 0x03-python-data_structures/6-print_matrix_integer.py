#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) != 0:
        rows = len(matrix)
        columns = len(matrix[0])
        for r in range(rows):
            for c in range(columns):
                if c == columns - 1:
                    print("{:d}".format(matrix[r][c]))
                else:
                    print("{:d}".format(matrix[r][c]), end=" ")
    else:
        print()
