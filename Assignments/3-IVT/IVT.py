"""
Ayaan Khan
735229
Assignment: IVT
File: ivt.py
Purpose: A class that has methods to get zeroes in a polynomial.
"""

from polynomial import Polynomial


class IVT:
    def __init__(self, polynomial):
        self.polynomial: Polynomial = polynomial

    def getZero(self, x1, x2, newtons=False):
        """
        Gets the x-intercept using the method of the user's choice. Defaults to IVT
        """
        # If the values of f(x1) and f(x2) share the same sign, return None, which represents no roots in this interval
        if self.polynomial.f(x1) * self.polynomial.f(x2) > 0:
            return None
        elif newtons:
            return self.newtons_method(x1, x2)
        return self.ivt(x1, x2)

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

        # Get the derivative, which is important for this method
        deriv = self.polynomial.derivative()

        found = False
        # Get the initial xn value
        xn = (x1 + x2) / 2
        while not found:
            # Get the next xn value
            xn1 = xn - self.polynomial.f(xn) / deriv.f(xn)

            # Compare the two. If they are sufficiently close enough, settle with this x value
            if round(xn, 3) == round(xn1, 3):
                found = True
                return xn1
            # Otherwise, continue with the loop, setting xn to its new value
            xn = xn1

    def ivt(self, x1, x2) -> float:
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

        found = False
        while not found:
            # Average the x1 and x2 valuesa and calculate f(x0)
            x0 = (x1 + x2) / 2
            fx0 = self.polynomial.f(x0)
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
