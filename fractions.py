import sys

def gcd(a,b):
    r = a%b
    while r:
        a,b=b,r
        r=a%b
    return b

class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __repr__(self):
        n = self.n//gcd(self.n, self.d) # simplify the fraction by calling the gcd function of numerator and denominator and then dividing the numerator by the result
        d = self.d//gcd(self.n, self.d) # simplify the fraction by calling the gcd function of numerator and denominator and then dividing the denominator by the result
        return f'{n}' if d == 1 else f'{n}/{d}'

    def add(self, f):
        n = self.n*f.d+f.n*self.d
        d = self.d*f.d
        return Fraction(n, d)

    def sub(self, f):
        n = self.n*f.d-f.n*self.d
        d = self.d*f.d
        return Fraction(n, d)

    def mul(self, f):
        n = self.n*f.n
        d = self.d*f.d
        return Fraction(n, d)

    def div(self, f):
        n = self.n*f.d
        d = self.d*f.n
        return Fraction(n, d)

out = []
ind = 0

for lines in sys.stdin:
    invalid = False
    op=a=b=None
    for i in lines:
        if i == '+':
            op = '+'
        elif i == '-':
            op = '-'
        elif i == '*':
            op = '*'
        elif i == '\\':
            op = '\\'
    line = lines.split(op)
    for i in line:
        if '/' in i: # check if the input is a fraction
            for c in range(len(i)):
                if i[c] == '/':
                    ind = c
            if not a:
                if int(i[ind+1:]) == 0: # check if the denominator of the first fraction is 0
                    invalid = True
                else:
                    a = Fraction(int(i[0:ind]), int(i[ind+1:]))
            elif not b:
                if int(i[ind+1:]) == 0 or (op == '\\' and int(i[0:ind]) == 0):
                    invalid = True
                else:
                    b = Fraction(int(i[0:ind]), int(i[ind+1:]))
        else: # if the input is not a fraction then it's an integer
            if not a:
                if int(i) == 0:
                    invalid = True
                else:
                    a = Fraction(int(i), 1)
            elif not b:
                if int(i) == 0:
                    invalid = True
                else:
                    b = Fraction(int(i), 1)

    if invalid:
        out.append('invalid')
    
    if not invalid:
        if op == '+':
            out.append(a.add(b))
        elif op == '-':
            out.append(a.sub(b))
        elif op == '*':
            out.append(a.mul(b))
        elif op == '\\':
            out.append(a.div(b))
                    
for i in out:
    print(i)
