class SplineSegment:
    def _init_(self, i, coef1, coef2, coef3=None, coef4=None, function_str=None):
        self.i = i
        self.coef1 = coef1
        self.coef2 = coef2
        self.coef3 = coef3
        self.coef4 = coef4
        self.function_str = function_str

    def _str_(self):
        return f"SplineSegment(i={self.i}, coef1={self.coef1}, coef2={self.coef2}, coef3={self.coef3}, coef4={self.coef4}, function='{self.function_str}')"
    
    def _repr_(self):
        return f"SplineSegment(i={self.i}, coef1={self.coef1}, coef2={self.coef2}, coef3={self.coef3}, coef4={self.coef4}, function='{self.function_str}')"