#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in range(len(matrix)):
        result.append(list(map(lambda x: x ** 2, matrix[i])))
    return result
