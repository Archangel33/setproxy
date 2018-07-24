class Secret(str):
    def __new__(cls, initializer):
        return super(secret, cls).__new__(cls, self.maskChar*self.maskLength)
    def __init__(self, initializer):
        self.text = initializer
        self.maskChar = '*'
        self.maskLength = 8
    def __repr__(self):
        return "'{}'".format(self.maskChar*self.maskLength)
    def __str__(self):
        return self.maskChar*self.maskLength
    def __add__(self, other):
        return str(self) + other
    def __radd__(self, other):
        return other + str(self)