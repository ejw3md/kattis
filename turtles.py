class Passings:
    def __init__(self, passing):
        self.passing = passing
        self.order = ord(passing[1])-ord(passing[0])
    def reOrder(self):
        if(self.order<0):
            self.order = -2*self.order
        else:
            self.order = 2*self.order-1
def printP(passes):
    for p in passes:
        print("%s %d" % (p.passing, p.order))
def ree(passes):
    for p in passes:
        p.reOrder()

turtles = [chr(x+ord('A')) for x in range(ord(input())-ord('A')+1)]

print(turtles)
p = int(input())
passes = [Passings(input()) for x in range(p)]
'''
for x in range(p):
    pas = Passings(input())
    passes.append(pas)
#printP(passes)
'''
d = dict()
for x in range(p):

ree(passes)
passes.sort(key = lambda x: x.order)
printP(passes)
