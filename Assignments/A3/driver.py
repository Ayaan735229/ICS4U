from polynomial import Polynomial

# Driver
P = Polynomial([0, 0, 1, 2, 0, -3])
print(P)
for i in range(10):
	print(i, P.f(i))
print()
print("Polynomial order:", P.get_order())
p_deriv = P.derivative()
print("Derivative:", p_deriv)
print("IVT:", P.ivt(0.5, 1.25))
print("Newton's method:", P.newtons_method(0.5, 1.25))
