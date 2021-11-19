#!/bin/python3

import math
import os
import random
import re
import sys
import copy

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
    lookupTable = [[0 for r in range(row)] for c in range(column)]
    lookupTable2 = copy.deepcopy(lookupTable)
    def findCollectMax(r1, c1, r2, c2):
        def downRight(r1, c1):
            for i in range(row):
                for j in range(column):
                    if i == j == 0:
                        lookupTable[i][j] = mat[i][j]
                    elif mat[i][j] == -1:
                        lookupTable[i][j] = mat[i][j]
                        continue
                    elif i == 0: #try reversing i and j in order in the if else chain
                        if lookupTable[i][j-1] == -1:
                            lookupTable[i][j] = mat[i][j]
                        else:
                            lookupTable[i][j] = lookupTable[i][j-1] + mat[i][j]
                            if j > 0:
                                mat[i][j-1] = 0
                    elif j == 0:
                        if lookupTable[i-1][j] == -1:
                            lookupTable[i][j] = mat[i][j]
                        else:
                            lookupTable[i][j] = lookupTable[i-1][j] + mat[i][j]
                            if i > 0:
                                mat[i-1][j] = 0
                    else:
                        lookupTable[i][j] = max(lookupTable[i][j-1], lookupTable[i-1][j]) + mat[i][j]
                        if lookupTable[i][j-1] > lookupTable[i-1][j] and mat[i][j-1] != -1:
                            mat[i][j-1] = 0
                        elif lookupTable[i][j-1] < lookupTable[i-1][j] and mat[i-1][j] != -1:
                            mat[i-1][j] = 0
            if mat[-1][-1] == 1:
                mat[-1][-1] = 0
            return lookupTable[-1][-1]
        
        def upLeft(r2, c2):
            for i in range(1 ,row+1):
                for j in range(1, column+1):
                    if -i == -j == -1:
                        lookupTable2[-i][-j] = mat[-i][-j]
                    elif mat[-i][-j] == -1:
                        lookupTable2[-i][-j] = mat[-i][-j]
                        continue
                    elif -i == -1:
                        if lookupTable2[-i][-j+1] == -1:
                            lookupTable2[-i][-j] = mat[-i][-j]
                        else:
                            lookupTable2[-i][-j] = lookupTable2[-i][-j+1] + mat[-i][-j]
                            if j < -1:
                                mat[-i][-j+1] = 0
                    elif -j == -1:
                        if lookupTable2[-i+1][-j] == -1:
                            lookupTable2[-i][-j] = mat[-i][-j]
                        else:
                            lookupTable2[-i][-j] = lookupTable2[-i+1][-j] + mat[-i][-j]
                            if i < -1:
                                mat[-i+1][-j] = 0
                    else:
                        lookupTable2[-i][-j] = max(lookupTable2[-i][-j+1], lookupTable2[-i+1][-j]) + mat[-i][-j]
                        if lookupTable2[-i][-j+1] > lookupTable2[-i+1][-j] and mat[-i][-j+1] != -1:
                            mat[-i][-j+1] = 0
                        elif lookupTable2[-i][-j+1] < lookupTable2[-i+1][-j] and mat[-i+1][-j] != -1:
                            mat[-i+1][-j] = 0
            return lookupTable2[0][0]
        
        drMax = downRight(r1, c1)
        ulMax = upLeft(r2, c2)
        if drMax == -1 or ulMax == -1:
            return 0
        else:
            return drMax+ulMax
    return max(0, findCollectMax(0,0,row-1,column-1))

if __name__ == '__main__':

    mat_rows = 3
    mat_columns = 3

    mat = [[0, 1, -1], 
           [1, 0, -1], 
           [1, 1, 1]]
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

    mat4 = [[0, -1, 1, 0, 0],
            [1, 0, -1, 0, 0],
            [1, -1, 1, -1, -1],
            [1, -1, 1, 1, 1],
            [0, 1, 1, 0, 0]]

    n = 100
    m = 100

    matrix = []
    matrix2 = []
    matrix3 = []
    with open('input011.txt') as f:
        for line in f:
            matrix.append(list(map(int, line.rstrip().split(" "))))

    with open('input013.txt') as e:
        for line in e:
            matrix2.append(list(map(int, line.rstrip().split(" "))))
    
    with open('input014.txt') as g:
        for line in g:
            matrix3.append(list(map(int, line.rstrip().split(" "))))
    """
    result = collectMax(mat)
    print(str(result) + '\n')
    print("Expected Result: 5")

  
    result = collectMax(mat2)
    print(str(result) + '\n')
    print("Expected Result: 11")

    result = collectMax(mat3)
    print(str(result) + '\n')
    print("Expected Result: 0")

    result = collectMax(matrix)
    print(str(result) + '\n')
    print("Expected Result: 312")

    result = collectMax(matrix2)
    print(str(result) + '\n')
    print("Expected Result: ?")
    """
    result = collectMax(mat4)
    print(str(result) + '\n')
    print("Expected Result: 5")

    result = collectMax(matrix3)
    print(str(result) + '\n')
    print("Expected Result: 16")


#3
#3
#0 1 -1
#1 0 -1
#1 1 1