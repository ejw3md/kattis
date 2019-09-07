def do_it():
    children = int(input())
    candies = 0
    for i in range(children):
        s = input()
        if len(s) > 20:
            s = s[:20]
        candies+=int(s)
    if candies % children == 0:
        print("YES")
    else:
        print("NO")




test_cases = int(input())
input()
for i in range(test_cases):
    do_it()
    if i != test_cases-1:
        input()