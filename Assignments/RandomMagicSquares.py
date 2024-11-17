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
    Precondition: have already gotten a number from the user

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


def getInitRow(dim, zeroed = False):
    """
    Creates the initial row for the square
    Precondition: Recieved a dimension from the user and ensured its validity

    dim (int)         The dimensions of the square
    zeroed (bool)     Determines the type of square

    initRow (int[])  First row of of the square
    """
    initRow = []
    if zeroed:
        # for every number, n, from 0 (inclusive) to dim (exclusive), add to the array n * dim
        initRow = [n * dim for n in range(dim)]
    else:
        # for every number, n, from 1 (inclusive) to dim + 1 (exclusive), add to the array n
        initRow = [n for n in range(1, dim+1)]
    # shuffle the array
    random.shuffle(initRow)
    
    return initRow


def generateTrivialMagicSquare(dim, shift, zeroed = False):
    """
    Generates a magic square given the initial row and the shift
    Precondition: Recieved a valid dimension from user and generated an initial row

    dim (int)       The dimensions of the square
    shift (int)     The shift to be used per row
    zeroed (bool)   Determines the type of square, to be passed to getInitRow

    intRow (int[])  The initial row, supplied by getInitRow
    M (int[][])     The generated trivial magic square
    """

    # Initialize the matrix with the first row
    initRow = getInitRow(dim, zeroed)
    M = []
    M.append(initRow)

    for i in range(dim-1):
        # Get the latest addition to the Matrix
        tempArr = M[len(M)-1]
        shiftedArr = []
        # Shift it and add it to the matrix
        for j in range(dim):
            shiftedArr.append(tempArr[(j + dim - shift) % dim])
        M.append(shiftedArr)
    return M


def addMatrices(M1, M2):
    """
    Takes two equal dimension matrices and adds them together
    Precondition: Have (created) two matrices 

    M1 (int[][]) The first matrix to add
    M2 (int[][]) The second matrix to add

    M (int[][]) The summed matrix
    """
    M = []
    # Add values from one matrix to the matching value in the other matrix
    for i in range(len(M1)):
        tempRow = []
        for j in range(len(M1)):
            tempRow.append(M1[i][j] + M2[i][j])
        M.append(tempRow)
        
    return M


def isMagic(M):
    """
    Checks whether a given matrix is a magic square, trivial or normal
    Precondition: Have a matrix to check

    M (int[][]) The matrix to be checked

    dim (int)           Dimensions of the matrix
    magicSum (int)      Supposed magic sum of the matrix
    diagMainSum (int)   Sum of the main diagonal
    diagSecSum (int)    Sum of the second diagonal
    currRowSum (int)    Sum of one row
    currColSum (int)    Sum of one row
    """

    dim = len(M)
    magicSum = calculateMagicSum(dim)
  
    # Check diagonal
    diagMainSum = 0
    diagSecSum = 0
    for i in range(dim):
        diagMainSum += M[i][i]
        diagSecSum += M[i][dim-i-1]
    # If the two aren't equal, return early
    if diagMainSum != diagSecSum != magicSum:
        return False
    
    # Check horizontal/vertical
    for i in range(dim):
        currRowSum = 0
        currColSum = 0
        for j in range(dim):
            currRowSum += M[i][j]
            currColSum += M[j][i]

        # Compare current row, current column, and the magic sum
        # If the three aren't equal, return early
        if currRowSum != currColSum != magicSum:
            return False
    
    # If the function has reached this, then the matrix is a magic square
    return True


def calculateMagicSum(dim):
    """
    Calculates the sum of the Magic Square
    Precondition: Have a valid magic square

    M (int[][]) The magic square

    magicSumArr (int[]) List of each term to be divided in the magic sum
    magicSum (int)      The magic sum
    """

    # Get a list of all the numbers from 1 (inclusive) to dim^2 + 1 (exclusive)
    magicSumArr = [n for n in range(1, dim**2+1)]
    magicSum = int(sum(magicSumArr)/dim)
    return magicSum


def matrixFormattedPrint(M):
    """
    Outputs a matrix in a cleaner, 3 column per number, format
    Precondition: Have a matrix

    M (int[][]) The matrix to be printed
    """
    print("Square One")
    for row in M:
        for num in row:
            # Print the number with a 3 col wide space, no new line
            print(f"{num:3d}", end=" ")
        # Print the line seperator
        print()
    

if __name__ == "__main__":
    # Assume that the provided value is NOT valid
    isValid = False
    
    while (not isValid):
        userDims = int(input("Enter a prime number from 5-19 (inclusive): "))
        # Update the validity of the inputted dimensions
        isValid = checkValidity(userDims)
    
    # Create both matrices and add them
    A = generateTrivialMagicSquare(userDims, 2)
    B = generateTrivialMagicSquare(userDims, 3, True)
    sumMatrix = addMatrices(A, B)

    magicSum = calculateMagicSum(userDims)
    
    # Print each matrix, formatted, the magic sum, as well as whether the final matrix is magic
    print("Square One")
    matrixFormattedPrint(A)
        
    print("\nSquare Two")
    matrixFormattedPrint(B)
    
    print("\nMagic Square")
    matrixFormattedPrint(sumMatrix)

    print("\nMagic Sum:", magicSum)
        
    print("This square is Magic:", isMagic(sumMatrix))
