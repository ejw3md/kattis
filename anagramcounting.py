import sys

def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret*=i
    return ret
def do_it(string):
    dividers = [0] * 123
    ans = factorial(len(string))
    for c in string:
        dividers[ord(c)]+=1
    for num in dividers:
        ans//=factorial(num)
    print(ans)

for line in sys.stdin:
    do_it(line[:-1])