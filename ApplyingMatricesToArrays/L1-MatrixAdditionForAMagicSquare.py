# Part 1
def make5x5(M, shift):
  matrix = []
  matrix.append(M.copy())
  dim = len(M)
    
  for i in range(dim-1):
    temp_row = []
    for j in range(dim):
      temp_row.append(matrix[i][(j + dim - shift) % dim])
    matrix.append(temp_row)
  return matrix
    
a1 = [5, 1, 4, 2, 3]    
b1 = [15, 20, 0, 10, 5]

A = make5x5(a1, 2)
B = make5x5(b1, 3)

print("make5x5(a1, 2)")
for row in A:
  print(row)
print("\nmake5x5(b1, 3)")
for row in B:
  print(row)


# Part 2
def addM(M1, M2):
  new_M = []
  for i in range(len(M1)):
    temp_row = []
    for j in range(len(M1)):
      temp_row.append(M1[i][j] + M2[i][j])
    new_M.append(temp_row)
    
  return new_M
  
print("\naddM(A, B)")
sum_M = addM(A, B)
for row in sum_M:
  print(row)


# Part 3
def isMagic(M):
  dim = len(M)
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

print("\nisMagic(sum_M)")
print(isMagic(sum_M))
