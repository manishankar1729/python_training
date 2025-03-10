# File: pkg/poly.py

class Poly:
    def __init__(self, *coefficients):
        """
        Initialize the polynomial with coefficients.
        Coefficients are passed in decreasing order of power (an, ..., a0).
        """
        self.coefficients = list(coefficients)

    def __add__(self, other):
        """
        Add two polynomials by aligning coefficients.
        """
        # Make both coefficient lists the same length by padding with zeros
        len_self = len(self.coefficients)
        len_other = len(other.coefficients)
        if len_self < len_other:
            self.coefficients = [0] * (len_other - len_self) + self.coefficients
        elif len_other < len_self:
            other.coefficients = [0] * (len_self - len_other) + other.coefficients
        
        # Add corresponding coefficients
        result_coeffs = [x + y for x, y in zip(self.coefficients, other.coefficients)]
        return Poly(*result_coeffs)

    def __str__(self):
        """
        Return a string representation of the polynomial.
        """
        terms = []
        degree = len(self.coefficients) - 1
        for power, coeff in enumerate(self.coefficients):
            if coeff != 0:
                if degree - power == 0:
                    terms.append(f"{coeff}")
                elif degree - power == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}x^{degree - power}")
        return " + ".join(terms) if terms else "0"
