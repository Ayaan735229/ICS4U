class Term:
    def __init__(self, coeff, degree):
        self.coeff = coeff
        self.degree = degree
        self.next = None

class Polynomial:
    def __init__(self, terms):
        self.length = 0
        self.head = None

        has_valid = False
        for i in range(len(terms)):
            if terms[i] == 0 and not has_valid:
                continue
            has_valid = True
            self.add_term(terms[i], len(terms)-i-1)

    def __str__(self) -> str:
        # TODO: check if I'm allowed to use an array
        poly_arr = []

        curr = self.head
        while (curr):
            if curr.coeff < 0:
                poly_arr.append("-")
            elif curr.coeff >= 0 and len(poly_arr) > 0:
                poly_arr.append("+")

            temp = str(abs(curr.coeff))

            # TODO: check whether the last term should be "ax^0" or just "a"
            # Conflicting things shown on document
            if (curr.degree):
                temp += "x"
                if curr.degree != 1:
                    temp += f"^{curr.degree}"
            
            poly_arr.append(temp)
            curr = curr.next
        return " ".join(poly_arr)

    def add_term(self, coeff, degree) -> "Polynomial":
        # TODO: check if each factor with a coeffecient of 0 really needs to be added
        # if coeff == 0:
        #     return None
        
        self.length += 1
        term = Term(coeff, degree)
        if not self.head:
            self.head = term
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
                
            curr.next = term

        return term
    
    def get_order(self) -> int:
        return max(self.length-1, 0)
            
    def f(self, x) -> float:
        poly_sum = 0

        curr = self.head
        while (curr):
            poly_sum += curr.coeff * (x ** curr.degree)
            curr = curr.next

        return poly_sum

    def derivative(self) -> "Polynomial":
        order = self.get_order()
        deriv_terms = [0]*(order-1)

        curr = self.head
        while (curr and curr.degree > 1):
            if curr.coeff == 0:
                curr = curr.next
                continue

            t_ceoff = curr.degree * curr.coeff
            deriv_terms[order-curr.degree] = t_ceoff
            curr = curr.next

        return Polynomial(deriv_terms)

    def ivt(self, x1, x2) -> float:
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

    def ivtLegacy(self, x1, x2) -> float:
        # alternatively, check if f(x1) < 0 and f(x2) > 0
        # if self.f(x1) < 0 and self.f(x2) > 0
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

