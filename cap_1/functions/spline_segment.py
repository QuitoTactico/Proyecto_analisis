class SplineSegment:
    def __init__(self, i, coef1, coef2, coef3=None, coef4=None, function_str=None):
        self.i = i
        self.coef1 = coef1
        self.coef2 = coef2
        self.coef3 = coef3
        self.coef4 = coef4
        self.function_str = function_str

    def __str__(self):
        return f"SplineSegment(i={self.i}, coef1={self.coef1}, coef2={self.coef2}, coef3={self.coef3}, coef4={self.coef4}, function='{self.function_str}')"
    
    def __repr__(self):
        return f"SplineSegment(i={self.i}, coef1={self.coef1}, coef2={self.coef2}, coef3={self.coef3}, coef4={self.coef4}, function='{self.function_str}')"