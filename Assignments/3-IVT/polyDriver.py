from polynomial import Polynomial
from polynomialLinkedList import Polynomial as PolynomialLL

# Driver
P = Polynomial([0, 0, 1, 2, 0, 3, 0, 0])
print(P)
for i in range(10):
	print(i, P.f(i))
print("Polynomial order:", P.get_order())
print("Derivative", P.derivative())
