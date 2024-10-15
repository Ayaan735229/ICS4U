"""
Ayaan Khan
735229
RandomMagicSquares.py

Generates a random magic square using a prime number ranging from 5 to 19.
"""

import math
import random


def checkValidity(n):
    """
    Checks the validity of a provided n for a magic square dimension 
    n (int) Potential dimensions for the magic square
    """
    # dims cannot be less than 5
    if n < 5 or n > 19:
        return False
    # Check every number from 2 to half of n to see if they're divisible
    # if they are, then n is NOT prime
    for i in range(2, math.floor(n/2)):
        if n % i == 0:
            return False
    return True


def initRow(dim, zeroed = False):
    """
    Creates the initial row for the square
    dim (int)         The dimensions of the square
    zeroed (bool)     Determines the type of square
    arr_init (int[])  First row of of the square
    """
    arr_init = []
    if zeroed:
        arr_init = [n * dim for n in range(0, dim)]
    else:
        arr_init = [n for n in range(1, dim+1)]
    random.shuffle(arr_init)
    
    return arr_init

def generateMagicSquare(dim, shift, zeroed = False):
    arr_init = initRow(dim, zeroed)
    M = []
    M.append(arr_init)

    for i in range(dim-1):
        tempArr = M[len(M)-1]
        shiftedArr = []
        for j in range(dim):
            shiftedArr.append(tempArr[(j + dim - shift) % dim])
        M.append(shiftedArr)
    return M

def addMatrices(M1, M2):
    new_M = []
    for i in range(len(M1)):
        temp_row = []
        for j in range(len(M1)):
            temp_row.append(M1[i][j] + M2[i][j])
        new_M.append(temp_row)
        
    return new_M

def isMagic(M):
    dim = len(M)
  
    # check diagonal
    diag_main_sum = 0
    diag_sec_sum = 0
    for i in range(dim):
        diag_main_sum += M[i][i]
        diag_sec_sum += M[i][dim-i-1]
    if diag_main_sum != diag_sec_sum:
        return False
    
    # check horizontal/vertical
    for i in range(dim):
        curr_row_sum = 0
        curr_col_sum = 0
    for j in range(dim):
        curr_row_sum += M[i][j]
        curr_col_sum += M[j][i]
      
    if curr_row_sum != curr_col_sum != diag_main_sum:
        return False
      
    return True

if __name__ == "__main__":
    isValid = False
    
    while (not isValid):
        user_dims = int(input("Enter a prime number from 5-19 (inclusive): "))
        isValid = checkValidity(user_dims)
    
    A = generateMagicSquare(user_dims, 2)
    B = generateMagicSquare(user_dims, 3, True)
    sumMatrix = addMatrices(A, B)
    
    print("Square One")
    for line in A:
        print(line)
        
    print("\nSquare Two")
    for line in B:
        print(line)
    
    print("\nFinal Magic Square")
    for line in sumMatrix:
        print(line)
        
    print(isMagic(sumMatrix))

