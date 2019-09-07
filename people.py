import math
class Coor:
    def __init__(self, r, c, val):
        self.r= r
        self.c = c
        self.val = val
    def __str__(self):
        return str(self.r) + " " + str(self.c)


def direction(s, arr, visited, right, up):
    return s.c+right<len(arr[s.r]) and s.c+right>=0 and s.r+up<len(arr) and s.r+up>=0 and s.val == arr[s.r+up][s.c+right] and not visited[s.r+up][s.c+right]


def distance(p1, p2):
    return math.sqrt((p1.r-p2.r)**2 + (p1.c-p2.c)**2)


def insert(queue, p, end):
    appended = False
    for i in range(len(queue)):
        if distance(p, end)<distance(queue[i], end):
            queue.insert(i, p)
            appended = True
            break
    if not appended:
        queue.append(p)
def printqueue(queue):
    for r in queue:
        print(r)

def search(arr, startR, startC, endR, endC):
    visited = []
    for i in range(len(arr)):
        visited.append([False]*len(arr[i]))
    queue = []
    end = Coor(endR, endC, arr[endR][endC])

    queue.append(Coor(startR, startC, arr[startR][startC]))
    visited[startR][startC] = True

    while queue and not (queue[0].r==endR and queue[0].c==endC):
        s = queue.pop(0)
        #append right
        if direction(s, arr, visited, 1, 0):
            insert(queue, Coor(s.r, s.c+1, s.val), end)
            visited[s.r][s.c+1]=True
        #append left
        if direction(s, arr, visited, -1, 0):
            insert(queue, Coor(s.r, s.c-1, s.val), end)
            visited[s.r][s.c-1]=True
        #append down
        if direction(s, arr, visited, 0, 1):
            insert(queue, Coor(s.r+1, s.c, s.val), end)
            visited[s.r+1][s.c]=True
        #append up
        if direction(s, arr, visited, 0, -1):
            insert(queue, Coor(s.r-1, s.c, s.val), end)
            visited[s.r-1][s.c]=True

    #check if weve reached the end
    if queue and queue[0].r==endR and queue[0].c==endC:
        if(queue[0].val == '1'):
            return "decimal"
        else:
            return "binary"
    return "neither"

def getMap():
    r, c = input().split()
    arr = []
    for x in range(int(r)):
        arr.append(list(input()))
    return arr
def printMap(arr):
    print("\n")
    for r in arr:
        for c in r:
            print(c,"", end="")
        print()


arr = getMap()
q = int(input())
for i in range(q):
    p = input().split()
    print(search(arr, int(p[0])-1, int(p[1])-1, int(p[2])-1, int(p[3])-1))
