def square(n):
    n = str(n)
    s = 0
    for x in range(len(n)):
        s+= int(n[x])**2
    return s
s89 = set()
s1 = set()
numeight = 0
temp = 0
try:
    for n in range(1, 10**8):
        temp = n
        if n==10**7:
            print("HI")
        all = [n]
        x = square(n)
        one = False
        eight = False
        while(x!=89 and x!=1):
            if x in s89:
                eight = True
                break
            elif x in s1:
                one=True
                break
            else:
                all.append(x)
            x = square(x)
        if(x==89 or eight):
            numeight+=1
            if(n<=10**6):
                for ans in all:
                    s89.add(ans)
        else:
            if(n<=10**4):
                for ans in all:
                    s1.add(ans)
except KeyboardInterrupt:
    print(temp)

print(numeight)
