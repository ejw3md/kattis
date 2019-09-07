def check(A, B, n):
    return n>=A and n<=B
def recur(A, B, n, curLen, s):
    #print(n, curLen)
    if len(n) == curLen//2:
        if curLen%2==0:
            if check(A, B, int(n[::-1]+n)):
                #print(n[::-1]+n)
                s.add(n[::-1]+n)
        else:
            if check(A, B, int(n[::-1]+'0'+n)):
                if check(A, B, int(n[::-1]+'1'+n)):
                    #print(n[::-1]+'0'+n)
                    #print(n[::-1]+'1'+n)
                    s.add(n[::-1]+'0'+n)
                    s.add(n[::-1]+'1'+n)
                else:
                    #print(n[::-1]+'0'+n)
                    s.add(n[::-1]+'0'+n)
            elif check(A, B, int(n[::-1]+'1'+n)):
                s.add(n[::-1]+'1'+n)
    elif(len(n)<curLen//2):
        recur(A, B, '0'+n, curLen, s)
        recur(A, B, '1'+n, curLen, s)
    return s
case = 0
while(True):
    case+=1
    A = int(input())
    B = int(input())
    if A==B and A==0:
        break
    palens = 0
    for x in range(len(str(A))+1, len(str(B))):
        palens+=2**((x+1)//2-1)
    #print(palens)
    s = set()
    if len(str(A))==1:
        if A==B:
            palens+=1
        elif(A==1):
            palens+=1
        else:
            palens+=2
    else:
        palens+= len(recur(A, B, '1', len(str(A)), s))
    #print(palens)
    if len(str(A)) != len(str(B)):
        s.clear()
        palens += len(recur(A, B, '1', len(str(B)), s))
    #print(temp)
    print("Case %d: %d" % (case, palens))
