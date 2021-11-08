#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'collectMax' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY mat as parameter.
#
    
def collectMax(mat):
    # Write your code here
    row = len(mat)
    column = len(mat[0])
    lookupTable = [[[None] * row for r in range(row)] for c in range(column)]
    def findCollectMax(r1, c1, r2, c2):
        if (row == r1 or r2 == 0 or column == c1 or c2 == 0 or mat[r1][c1] == -1 or mat[r2][c2] == -1):
            return 0
        elif r1 == c1 == (row - 1):
            return mat[r1][c1]
        elif lookupTable[r1][c1][c2] is not None:
            return lookupTable[r1][c1][c2]
        else:
            maxCollect = mat[r1][c1] + (c1 == c2 and r1 == r2) * mat[r2][c2]
            maxCollect += max(findCollectMax(r1, c1+1, r2, c2-1), findCollectMax(r1+1, c1+1, r2-1, c2-1), findCollectMax(r1, c1+1, r2-1, c2), findCollectMax(r1+1, c1, r2, c2))
        lookupTable[r1][c1][c2] = maxCollect
        return maxCollect
    return max(0, findCollectMax(0,0,row-1,column-1))

if __name__ == '__main__':

    mat_rows = 3
    mat_columns = 3

    mat = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
    mat2 = [[1, 1, -1, 1, 1],
        [1, 0, 0, -1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, 1, 1, 1],
        [1, 1, -1, -1, 1]]
    mat3 = [[1, 1, -1, 1, 1],
        [1, 0, 0, -1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, 1, 1, 1],
        [1, 1, -1, -1, -1]]
    result = collectMax(mat)

    print(str(result) + '\n')
    print("Expected Result: 5")

    result = collectMax(mat2)
    print(str(result) + '\n')
    print("Expected Result: 9")

    result = collectMax(mat3)
    print(str(result) + '\n')
    print("Expected Result: 0")


#3
#3
#0 1 -1
#1 0 -1
#1 1 1