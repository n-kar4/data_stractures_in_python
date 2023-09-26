class myComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def print(self):
        print(f"{self.real} + {self.imag}i")
    
    def add(self, other):
        self.real = self.real + other.real
        self.imag = self.imag + other.imag
    def subtract(self, other):
        self.real = self.real - other.real
        self.imag = self.imag - other.imag
    def multiply(self, other):
        self.real = (self.real * other.real) - (self.imag * other.imag)
        self.imag = (self.real * other.imag) + (self.imag * other.real)

if __name__ == "__main__":
    c1 = myComplexNumber(4,-7)
    c2 = myComplexNumber(5,6)
    #c1.add(c2)
    c1.print()
    c1.multiply(c2)
    c1.print()