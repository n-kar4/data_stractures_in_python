class A:
    def __init__(self,x):
        self.x = x
        print('Im 1st  class A')
    def aaaa(self):
        return self.x*self.x

class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print('Im 2nd class B')
    def aaaa(self):
        return self.x*self.y

class C:
    def __init__(self):
        print('Im 3rd class C')
        super().__init__()
    



if __name__ == '__main__':
    s1 = A(5)
    print(s1.aaaa())

