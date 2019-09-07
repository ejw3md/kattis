def to_2(num, bits):
    ans=""
    bits-=1
    while bits>=0:
        if 2**bits <= num:
            num-= 2**bits
            ans+='1'
        else:
            ans+='0'
        bits-=1
    return ans
palendromes = 0
nth = int(input())
nth-=1
n = 0
length = 1
while n+2**((length-1)//2) <= nth:
    n += 2**((length-1)//2)
    length+=1
if nth == 0:
    palendrome = '1'
else:
    nth-=n
    palendrome = "1" + "0"*(length-2) + "1"
    if length%2 == 0:
        middle = to_2(nth, (length-2)//2)
        palendrome = '1' + middle +  middle[::-1] + '1'
    else:
        if nth == 0:
            pass
        elif nth==1:
            palendrome = palendrome[:len(palendrome)//2] + '1' + palendrome[len(palendrome)//2+1:]
        else:
            middle = to_2(nth, (length-1)//2)
            palendrome = '1' + middle +  middle[::-1][1:] + '1'
print(int(palendrome, 2))