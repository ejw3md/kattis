def convert_2(num):
    i = 2
    ans = ""
    while(i>=0):
        if 2**i <= num:
            ans+="1"
            num-=2**i
        else:
            ans+="0"
        i-=1
    return ans
def convert_16(num):
    tot = 0
    for n in range(len(num)):
        if num[n] =='1':
            tot+=2**(4-n-1)
    if tot> 9:
        if tot == 10:
            return 'A'
        elif tot==11:
            return 'B'
        elif tot==12:
            return 'C'
        elif tot==13:
            return 'D'
        elif tot==14:
            return 'E'
        elif tot==15:
            return 'F'
    return str(tot)
        
        
number = input()
binary = ""
for c in number:
    b = convert_2(int(c))
    binary +=b
if len(binary)%4!=0:
    binary="".join(['0'] * (4-len(binary)%4)) + binary 
ans=""
for c in range(0, len(binary), 4):
    ans+=convert_16(binary[c:c+4])
i = 0
while ans != '0' and ans[i] == '0':
    i+=1
print(ans[i:])