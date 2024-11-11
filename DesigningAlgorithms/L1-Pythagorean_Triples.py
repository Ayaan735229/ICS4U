def pythagTripBad():
	for a in range(1, 101, 1):
			for b in range(1, 101, 1):
					for c in range(1, 101, 1):
							left = a**2 + b**2
							right = c**2
							if left == right:
									print((a, b, c))

def pythagTrips(n):
	allTriples = []
	for a in range (3,n+1):
		if a % 2 == 0:
			temp = a**2 // 4
			b = temp - 1
			c = temp + 1
		else:
			temp = a // 2
			b = temp * (a + 1)
			c = b + 1
		
		allTriples.append((a, b, c))
	
	return allTriples

for triples in pythagTrips(12):
	print(triples)
