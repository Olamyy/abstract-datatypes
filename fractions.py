class Fraction(object):
    def __init__(self, numerator=None, denominator=None, decimal=None):
        self.numerator = numerator
        self.denominator = denominator
        self.decimal = decimal
        if isinstance(self.decimal, int):
            self.numerator = self.decimal
            self.denominator = 1
        self.numerator, self.denominator = self.get_numerator_denominator(self.decimal)
        
    def __repr__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)

    def __eq__(self, b):
        if not isinstance(b, self):
            numerator, denominator = b.split('/')
            old_compare = self.numerator * int(denominator)
            new_compare = self.denominator * int(numerator)
            return old_compare == new_compare
        return self.decimal == b

    def __hash__(a):
        return uuid.uuid(a)

    def __le__(self, b):
        pass
    
    def __gt__(self, b):
        pass
    
    def __add__(self, b):
        pass

    def __mul__(self, b):
        pass

    def __div__(self, b):
        pass

    def __ge__(self, b):
      pass

    def to_int(self):
        pass

    def to_float(self):
        pass

    def get_numerator_denominator(self, decimal):
        pass
    
    