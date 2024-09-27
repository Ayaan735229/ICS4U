a = [7, 1, 3, 5, 2, 4, 6]
b = []

for i in range(len(a)):
  b.append(a[(i + 5) % len(a)])

print(a)
print(b)
