class Poly:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)

    def __add__(self, other):
        len_self = len(self.coefficients)
        len_other = len(other.coefficients)
        if len_self < len_other:
            self.coefficients = [0] * (len_other - len_self) + self.coefficients
        elif len_other < len_self:
            other.coefficients = [0] * (len_self - len_other) + other.coefficients
        result_coeffs = [x + y for x, y in zip(self.coefficients, other.coefficients)]
        return Poly(*result_coeffs)

    def __str__(self):
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
