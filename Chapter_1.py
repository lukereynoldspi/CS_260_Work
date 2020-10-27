class Fraction:

    def __init__(self,top,bottom):
        if isinstance(top, int) != True or isinstance(bottom, int) != True :
            raise ValueError("The value(s) given are not integers!")
        else:
            common = self.gcd(top, bottom)
            self.num = int(top / common)
            self.den = int(bottom / common)



    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newdem = self.den * otherfraction.den

        return Fraction(newnum,newdem)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)


    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num

        return Fraction(newnum, newden)

e = Fraction(2, 1.0)
print(e.getDen())

