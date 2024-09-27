def linsearch(arr):
  duplicates = []
  for i in range(len(arr)):
    if arr[i] in duplicates:
      continue
    if arr.count(arr[i]) > 1:
      duplicates.append(arr[i])
      
  return duplicates or "Value Not Found"

myArr = [20, 20, 24, 27, 39, 40, 43, 46, 50, 
         60, 60, 62, 71, 74, 76, 86, 86, 87, 97, 97]

print(linsearch(myArr))
