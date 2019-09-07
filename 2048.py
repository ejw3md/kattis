def scan():
    x = []
    for i in range(4):
        x.append([int(s) for s in input().split()])
    return x
def printBoard(board):
    for x in board:
        for y in x:
            print("%d "%y, end="")
        print()
def neighbors(board, direction):
    if direction == 0:
        for x in range(len(board)):
            shiftLeft(board[x])
    elif direction == 2:
        for x in range(len(board)):
            shiftRight(board[x])
def shiftLeft(r):
    curEl = len(r)-1
    while(curEl>=0): #go through every element
        i = curEl-1
        while r[i] == 0 and i>0: #go left through the array until we find a nonzero
            i-=1
        if i == 0 and r[i]==0:
            r[0] = r[curEl]
            break
        if r[curEl]==r[i]: #if theyre equal then join them
            r[i]*=2
            r[curEl]=0
        else: #else shift the curElement to one element to the right of the nonzero element
            r[i+1] = r[curEl]
        curEl=i
    for i in range(len(r)-1):
        if r[i]==0 and r[i+1]!=0:
            r[i] = r[i+1]
            r[i+1] = 0
def shiftRight(r):
    curEl = 0
    while(curEl<len(r)): #go through every element
        i = curEl+1
        while i<len(r)-1 and r[i] == 0 : #go left through the array until we find a nonzero
            i+=1
        if i == 3 and r[i]==0:
            r[0] = r[curEl]
            break
        if r[curEl]==r[i]: #if theyre equal then join them
            r[i]*=2
            r[curEl]=0
        else: #else shift the curElement to one element to the right of the nonzero element
            r[i+1] = r[curEl]
        curEl=i
    for i in range(len(r)-1, 0. -1):
        if r[i]==0 and r[i-1]!=0:
            r[i] = r[i-1]
            r[i-1] = 0
board = scan()
direction = int(input())
neighbors(board, direction)
printBoard(board)




def findCommonRowRight(r):
    curEl = 0
    while(curEl<len(r)-2):
        if(r[curEl]==0):
            r[curEl] = r[curEl+1]
            r[curEl+1]=0
            curEl+=1
            continue
        i = curEl+1
        while(i<len(r) and r[i]==0):
            i+=1
        if i == len(r):
            curEl+=i
            continue
        if(r[curEl] == r[i]):
            r[curEl]*=2
            r[i] = 0
        else:
            if i!=curEl+1:
                r[curEl+1] = r[i]
                r[i] = 0
        curEl+=i
