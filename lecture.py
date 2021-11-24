class Vector:
    def __init__(self, *args):
        self.a = args

    def __repr__(self):
        return f'[{" ".join([str(x) for x in self.a])}]'

    def __add__(self, w):
        assert len(self.a) == len(w.a)
        sum = []
        for i in range(len(self.a)):
            sum.append(self.a[i]+w.a[i])
        return Vector(*sum)

    def __eq__(self, w):
        return self.a == w.a
    
class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, x):
        n = Node(x, self.head)
        self.head = n

    def pop(self):
        x = self.head.val
        self.head = self.head.next
        return x
    
class StatStack(Stack):
    def __init__(self):
        super().__init__()
        self.total = 0
        self.count = 0

    def push(self, x):
        super().push(x)
        self.total  += x
        self.count += 1

    def pop(self):
        x = super().pop()
        self.total -= x
        self.count -= 1
        return x
    
    def sum(self):
        return self.total

    def avg(self):
        return self.total/self.count