class Calk:

    def __init__ (self,a,b):
        self.a = a
        self.b = b

    def info(self):
        print (f"{self.a + self.b}")

    def info3(self):
        print (f"{self.a - self.b}")

    def info1(self):
        print (f"{self.a * self.b}")

    def info2(self):
        print (f"{self.a / self.b}")

    def __del__ (self):
        print ("")
     

def bis():
        B = Calk(a = int(input()),b = int(input()))
        B.info()
        B.info1()
        B.info2()
        B.info3()
bis()

