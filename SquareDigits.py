def square(n):
    n = str(n)
    s = 0
    for x in range(len(n)):
        s+= int(n[x])**2
    return s
d = dict()
s = set()
eight = 0
for n in range(1, 1000):
    x = square(n)
    while(x!=89 and x!=1):
        if x in s:
            d[str(x)]+=1
        else:
            d[str(x)]=1
            s.add(x)
        x = square(x)
    if(x==89):
        eight+=1
print(eight)
