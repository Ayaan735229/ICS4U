arr1 = [2, 8, 6, 3, 9, 1, 7]
arr2 = [0] * 7

for i in range(len(arr1)):
    arr2[i] = arr1[(i + 2) % len(arr1)]

print(arr1)
print(arr2)
