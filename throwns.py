def throw(start, index, n):
    start+=index
    if start<0:
        start+=n
    start%=n
    return start
if __name__ == "__main__":
    first = input()
    first = first.split()
    n = int(first[0])
    a = input().split()
    isundo=False
    undos = []
    start=0
    for i in range(len(a)):
        if(isundo):
            for j in range(int(a[i])):
                start = throw(start, -1*undos[-1], n)
                del undos[-1]
            isundo=False
            continue
        if a[i] == "undo":
            isundo=True
            continue
        start = throw(start, int(a[i]), n)
        undos.append(int(a[i]))
    print(start)