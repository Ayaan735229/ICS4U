def make5x5(M, shift):
  matrix = []
  matrix.append(M.copy())
  m_dim = len(M)
    
  for i in range(m_dim-1):
    tempRow = []
    for j in range(m_dim):
      tempRow.append(matrix[i][(j + (m_dim - shift)) % m_dim])
    matrix.append(tempRow)
  return matrix
    
a1 = [5, 1, 4, 2, 3]
b1 = [15, 20, 0, 10, 5]

A = make5x5(a1, 2)
B = make5x5(b1, 3)

for row in A:
  print(row)

for row in B:
  print(row)
