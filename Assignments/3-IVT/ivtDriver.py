from polynomial import Polynomial
from IVT import IVT

P = Polynomial([0, 0, 1, 2, 0, 3, 0, 0])
ivtObj = IVT(P)
print("IVT Method", ivtObj.getZero(-2.5, -2.4))
print("Newton's Method", ivtObj.getZero(-2.5, -2.4, True))
