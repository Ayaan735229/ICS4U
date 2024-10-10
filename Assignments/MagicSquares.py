import math
import random

def checkValidity(n):
    # dims cannot be less than 5
    if n < 5 or n > 19:
        return False
    # dims must be prime
    for i in range(2, math.floor(n/2)):
        if n % i == 0:
            return False
    return True

def initRow(dim, zeroed = False):
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
    
    for line in M:
        print (line)
    print("\n")
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

A = generateMagicSquare(5, 2)
B = generateMagicSquare(5, 3, True)
sumMatrix = addMatrices(A, B)

print(isMagic(sumMatrix))	

