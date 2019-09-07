# Enter your code here. Read input from STDIN. Print output to STDOU
rows = input().split(" ")
cols = int(rows[1])
rows = int(rows[0])
middle = False
for i in range(rows):
    for j in range(0, cols, 3):
        if i == rows//2:
            middle = True
            s = "-"*((cols-7)//2) + "WELCOME" + "-"*((cols-7)//2)
            print(s, end="")
            break
        elif(not middle and (j < (cols-3)/2 - i*3 or j>= (cols+3)/2 + i*3)):
            print("---", end="")
        elif middle and (j < (cols-3)/2 - (rows-1-i)*3 or j>= (cols+3)/2 + (rows-i-1)*3):
            print("---", end="")
        else:
            print(".|.", end="")
    print()