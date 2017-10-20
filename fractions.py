class Fraction(object):
    def __init__(self, numerator=None, denominator=None, decimal=None):
        self.numerator = numerator
        self.denominator = denominator
        self.decimal = (self.numerator / self.denominator) if not decimal else float(decimal)
        if isinstance(self.decimal, int):
            self.numerator = self.decimal
            self.denominator = 1
        elif isinstance(self.decimal, float):
            self.numerator, self.denominator = self.get_numerator_denominator(self.decimal)
        
    def __repr__(self):
        return "Fraction : {0}/{1} with Decimal: {2}".format(self.numerator, self.denominator, self.decimal)

    def __eq__(self, fraction):
        if not isinstance(fraction, self):
            numerator, denominator = fraction.split('/')
            old_compare = self.numerator * int(denominator)
            new_compare = self.denominator * int(numerator)
            return old_compare == new_compare
        return self.decimal == fraction

    def __le__(self, fraction):
        fraction = self.normalize_fraction(fraction)
        return self.decimal < fraction
    
    def __gt__(self, fraction):
         fraction = self.normalize_fraction(fraction)
         return self.decimal > fraction
    
    def __add__(self, fraction, output_as=None):
        fraction = self.normalize_fraction(fraction)
        fraction_sum = self.decimal + fraction
        return fraction_sum

    def __mul__(self, fraction):
        pass

    def __div__(self, fraction):
        pass

    def __ge__(self, fraction):
        pass

    def to_int(self):
        pass

    def to_float(self):
        pass

    def get_numerator_denominator(self, decimal):
        checker = (decimal).as_integer_ratio()
        return checker[0], checker[1]

    def normalize_fraction(self, fraction):
        if isinstance(fraction, Fraction):
            return fraction.decimal
        if isinstance(fraction, int) or isinstance(fraction, float):
            return float(fraction)
        numerator, denominator = fraction.split('/')
        return numerator / denominator

        
    

fraction = Fraction(decimal=0.3)
b = Fraction(decimal=10)

print(fraction.__add__(0.7))

print(fraction + 0.7)