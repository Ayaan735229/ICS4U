# TODO: add file information for both driver.py and polynomial.py
import math, time

class Term:
    def __init__(self, coeff, degree):
        self.coeff = coeff
        self.degree = degree

class Polynomial:
    def __init__(self, terms):
        temp_terms = {}

        has_valid = False
        for i in range(len(terms)):
        # TODO: check if each factor with a coeffecient of 0 really needs to be added
            if terms[i] == 0 and not has_valid:
                continue

            has_valid = True
            deg = len(terms)-i-1
            temp_terms[deg] = terms[i]

        self.terms = temp_terms

    def __str__(self) -> str:
        poly_arr = []

        for deg in self.terms.keys():
            coeff = self.terms[deg]
            if coeff < 0:
                poly_arr.append("-")
            elif coeff >= 0 and len(poly_arr) > 0:
                poly_arr.append("+")

            temp = str(abs(coeff))

            # TODO: check whether the last term should be "ax^0" or just "a"
            # Conflicting things shown on document
            if (deg):
                temp += "x"
                # if deg < 2:
                if deg != 1:
                    temp += f"^{deg}"
            
            poly_arr.append(temp)
        return " ".join(poly_arr)
    
    def get_order(self) -> int:
        return max(self.terms.keys())
            
    def f(self, x) -> float:
        poly_sum = 0

        for deg in self.terms.keys():
            if self.terms[deg] == 0:
                continue

            poly_sum += self.terms[deg] * (x ** deg)
        return poly_sum

    def derivative(self) -> "Polynomial":
        order = self.get_order()
        deriv_terms = [0]*(order-1)

        for deg in self.terms.keys():
            coeff = self.terms[deg]
            if deg < 2 or coeff == 0:
                continue
            t_ceoff = deg * coeff
            deriv_terms[order-deg-1] = t_ceoff

        return Polynomial(deriv_terms)

    def newtons_method(self, x1, x2) -> float:
        if self.f(x1) * self.f(x2) >= 0:
            return None
        
        deriv = self.derivative()
        
        found = False
        xn = (x1+x2)/2
        while not found:
            xn1 = xn - self.f(xn)/deriv.f(xn)

            if round(xn, 3) == round(xn1, 3):
                found = True
                return round(xn1, 4)
            xn = xn1

    def ivt(self, x1, x2) -> float:
        if self.f(x1) * self.f(x2) >= 0:
            return None

        found = False
        while not found:
            x0 = (x1+x2)/2
            fx0 = self.f(x0)
            n = round(fx0, 3)

            if n < 0.000:
                x1 = x0
            elif n > 0.000:
                x2 = x0
            else:
                found = True

        # TODO: check if we round x as well
        return x0

