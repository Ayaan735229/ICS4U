import math

A = [3, 2, 0, -1]
B = [5, 7, 8, 4]

# Problem 1
def addArray(arr1, arr2):
  newArr = [0]*len(arr1)
  
  for i in range(len(A)):
    newArr[i] = arr1[i] + arr2[i]
  
  return newArr
  
def getMagnitude(arr):
  tempSum = 0
  
  for i in range(len(arr)):
    tempSum += arr[i]**2
  
  return math.sqrt(tempSum)
  
# Problem 2a
def dotProduct(arr1, arr2):
  product = 0
  for i in range(len(arr1)):
    product += arr1[i] * arr2[i]
  
  return product

# Problem 2b
def getAngle(arr1, arr2):
  dProd = dotProduct(arr1, arr2)
  arr1M, arr2M = getMagnitude(arr1), getMagnitude(arr2)
  
  ratio = dProd / (arr1M * arr2M)
  deg = math.degrees(math.acos(ratio))
  return(deg)

# Problem 2c
ADProd = dotProduct(A, A)
AMag = getMagnitude(A)

print(ADProd, AMag**2)
  
print(addArray(A, B))

print(getAngle(A, B))
