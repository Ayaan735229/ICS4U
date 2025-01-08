# TODO: add file information for both driver.py and polynomial.py
# TODO: add more types and pre-reqs for each function

class Term:
    """
    Simple class which represents each term of a polynomial. A degree of zero turns the term into a constant.

    self.coeff (int)    The coefficient, or "a" value of the term.
    self.degree (int)   The degree to which x is raised.
    """
    def __init__(self, coeff, degree):
        self.coeff = coeff
        self.degree = degree

class Polynomial:
    """
    Polynomial class, with certain useful functions.

    self.terms (dict<int,int>)  Dictonary representation of the polynomial
    """
    def __init__(self, terms):
        """
        Initializes the polynomial.

        terms   (int[])             List of terms, where each degree is represented by position and the coeffecient by value

        terms_dict (dict<int,int>)  Dictonary which is a much clearer representation of the polynomial
        has_valid (bool)            Use to make sure the leading term has a non-zero value
        deg (int)                   Degree of a single term
        """
        terms_dict = {}

        has_valid = False
        for i in range(len(terms)):
        # TODO: check if each factor with a coeffecient of 0 really needs to be added
            # If the curr term essentially has a value of 0 and non-zero terms have not been reached, continue
            if terms[i] == 0 and not has_valid:
                continue

            # If this section part has been reached, then the above if statement is false
            # Therefore, set has_valid to True
            has_valid = True
            # Calculate the degree
            deg = len(terms)-i-1
            # Set the value of the coeffecient matching to the coefficient in the dictionary
            terms_dict[deg] = terms[i]

        # Set the classwide terms object
        self.terms = terms_dict

    def __str__(self) -> str:
        """
        Converts the polynomial into a easily readable-string

        poly_arr (str[])    Array of all the parts of the equations.
        deg (int)           A single term's degree.
        coeff (int)         A single term's coefficient.
        temp (str)          The combination of the term's coefficient and x^degree.

        return (str)        The contents of poly_arr joined with a space, aka a readable version of the polynomial
        """
        poly_arr = []

        # Loop over each key (degree) in self.terms
        for deg in self.terms.keys():
            coeff = self.terms[deg]
            # The curr term should start with a - if its negative
            if coeff < 0:
                poly_arr.append("-")
            # Otherwise it starts with +, as long as part of the polynomial has already been added
            elif coeff >= 0 and len(poly_arr) > 0:
                poly_arr.append("+")

            # Set the absolute value of the coefficient as the start of the term
            temp = str(abs(coeff))

            # TODO: check whether the second last term should be "ax^1" or just "ax"
            # Conflicting things shown on document
            # If the degree isn't 0, the term needs to be multiplied by x
            if (deg):
                temp += "x"
                # If the degree is low enough, there's no need for the "^"
                # if deg < 2:
                if deg != 1:
                    temp += f"^{deg}"
            
            # Add this to the array
            poly_arr.append(temp)
            # Join with a "+" so that it looks nice
        return " ".join(poly_arr)
    
    def get_order(self) -> int:
        """
        Gives the order of the polynomial.
        
        return (int)    The order.
        """
        # Since self.terms.keys() technically returns the degrees, the max of it is the polynomial order
        return max(self.terms.keys())
            
    def f(self, x) -> float:
        """
        Returns the value the polynomial when used as a function.

        x (float)           The x value to substitute x for in the function.

        poly_sum (float)    The answer.
        deg (int)           Degree of the curr term.

        return (float)      poly_sum
        """
        poly_sum = 0

        for deg in self.terms.keys():
            if self.terms[deg] == 0:
                continue

            poly_sum += self.terms[deg] * (x ** deg)
        return poly_sum

    def derivative(self) -> "Polynomial":
        """
        Returns the Polynomial form of this polynomial's derivative.

        order (int)         Order of this polynomial.
        d_terms (int[])     Each term of the derivative as an array.
        deg (int)           Degree of a single term from this polynomial.
        coeff (int)         Coefficient of a single term from this polynomial.
        d_coeff (int[])     Coeffcient of a single term from the derivative.
        idx (int[])         Index of a singular term from the derivative

        return (Polynomial) The derivative represented with the Polynomial class
        """
        # Get the order
        order = self.get_order()
        # Create a temporary array with 1 smaller than the original polynomial
        # i.e. this array represents a polynomial with 1 lower order
        d_terms = [0]*(order)

        for deg in self.terms.keys():
            coeff = self.terms[deg]
            # The derivative of a constant is 0, so we don't need it
            if deg < 1 or coeff == 0:
                continue
            # Using the power rule, f'(ax^n) = anx^(n-1)
            d_coeff = deg * coeff
            # Similar method to the one used in __init__ subtracted
            idx = order-deg
            # Set the value at the current index
            d_terms[idx] = d_coeff

        # Using the array, create a Polynomial object and return it
        return Polynomial(d_terms)

    # TODO: check if the return statement is supposed to be rounded
    # Also check if this should take 1 or 2 x values as parameters
    def newtons_method(self, x1, x2) -> float:
        """
        Calculates a single root using Newton's method, given two points.
        
        x1 (float)          An x value where f(x) < 0.
        x2 (float)          An x value where f(x) > 0.
        Or viceversa

        deriv (Polynomial)  The derivative of this polynomial.
        found (bool)        Represents whether the root has been found.
        xn (float)          Current x value to check
        xn1 (float)         The next xn value to compare to

        return (float)      An approximation of a root, i.e. one of the xn1 values
        """
        
        # If the values of f(x1) and f(x2) share the same sign, return None, which represents no roots in this interval
        if self.f(x1) * self.f(x2) >= 0:
            return None
        
        # Get the derivative, which is important for this method
        deriv = self.derivative()
        
        found = False
        # Get the initial xn value
        xn = (x1+x2)/2
        while not found:
            # Get the next xn value
            xn1 = xn - self.f(xn)/deriv.f(xn)

            # Compare the two. If they are sufficiently close enough, settle with this x value
            # TODO: Check which decimal to compare upto (i.e. what to round to here)
            if round(xn, 3) == round(xn1, 3):
                found = True
                return xn1
            # Otherwise, continue with the loop, setting xn to its new value
            xn = xn1

    def ivt(self, x1, x2) -> float:
        # TODO: check if the interval HAS to be +- 0.0004 or can it be +- 0.000499999, which this kinda uses
        """
        Calculates a single root using the Intermediate Value Theorem, given two points.

        x1 (float)      An x value where f(x) < 0.
        x2 (float)      An x value where f(x) > 0.
        Or viceversa

        found (bool)    Represents whether the root has been found.
        x0 (float)      A potential x intercept.
        fx0 (float)     The value of f(x0).
        n (float)       The rounded version to compare of fx0.
        """

        # If the values of f(x1) and f(x2) share the same sign, return None, which represents no roots in this interval
        if self.f(x1) * self.f(x2) >= 0:
            return None

        found = False
        while not found:
            # Average the x1 and x2 valuesa and calculate f(x0)
            x0 = (x1+x2)/2
            fx0 = self.f(x0)
            n = round(fx0, 3)

            # If n is less than 0, the root is in between x0 and x2, therefore x1 should now equal x0
            if n < 0.000:
                x1 = x0
            # If n is less than 0, the root is in between x1 and x0, therefore x2 should now equal x0
            elif n > 0.000:
                x2 = x0
            # Otherwise, a close enough value of x0 has been found
            else:
                found = True

        return x0

