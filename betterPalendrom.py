def check(A, B, n):
    return n>=A and n<=B
def recur(A, B, n, curLen, s):
    #print(n, curLen)
    if len(n) == curLen//2:
        if curLen%2==0:
            if check(A, B, int(n[::-1]+n)):
                #print(n[::-1]+n)
                s.add(n[::-1]+n)
                recur(A, B, '1', curLen+1, s)
        else:
            if check(A, B, int(n[::-1]+'0'+n)):
                if check(A, B, int(n[::-1]+'1'+n)):
                    #print(n[::-1]+'0'+n)
                    #print(n[::-1]+'1'+n)
                    s.add(n[::-1]+'0'+n)
                    s.add(n[::-1]+'1'+n)
                    recur(A, B, '1', curLen+1, s)
                else:
                    #print(n[::-1]+'0'+n)
                    s.add(n[::-1]+'0'+n)
                    recur(A, B, '1', curLen+1, s)
    elif(len(n)<curLen//2 and curLen<= len(str(B))):
        recur(A, B, '0'+n, curLen, s)
        recur(A, B, '1'+n, curLen, s)
    return s
case = 0
while(True):
    case+=1
    A = int(input())
    B = int(input())
    if A == B and A==0:
        break
    temp=0
    s = set()
    if len(str(A)) == 1:
        if(A==1):
            s.add('1')
        else:
            s.add('1')
            s.add('0')
        temp = recur(A, B, '1', 2, s)
    else:
        temp=recur(A, B, '1', len(str(A)), s)
    #print(temp)
    print("Case %d: %d" % (case, len(temp)))
