class Stack(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def delete(self):
        self.items = []
OPTR = Stack()
OPND = Stack()
intNumber = []
for n in range(10):
    intNumber.append(str(n))
def isInt(x):
    for n in intNumber:
        if(x == n): return 1
    return 0
def LISPadd(str):
    sum = 0
    i = 0
    s = list(str)
    while(True):
        if(s[i] != ')'):
            OPTR.push(s[i])
            #print(OPTR.items)
        else:
            OPND = Stack()
            while(OPTR.peek() != '+'):
                OPND.push(OPTR.pop())
            for t in OPND.items:
                sum += int(t)
            OPTR.pop()
            OPTR.pop()
        if(OPTR.is_empty() == True):
            break
        i += 1
    return sum
a = "(+(+(+12)(+34))(+(+56)(+78)))"
b = "(+45)"
print(LISPadd(a))