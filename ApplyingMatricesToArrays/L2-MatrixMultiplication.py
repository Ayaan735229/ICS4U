def mmult(P, Q):
  lenQ = len(Q)
  lenP = len(P)
  R = [[0], [0]]
  
  for i in range(lenQ):
    tempSum = 0
    for j in range(lenP):
      tempSum += Q[i][j] * P[j][0]
    
    R[i][0] = tempSum
  
  return R

Q = [[0.5, 1.4, 1], [1, 2, 0.5]]
P = [[2.20], [3.10], [2.60]]

R = mmult(P, Q)
print(R)
