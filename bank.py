class Person:
    def __init__(self, crowns, time):
        self.crowns = crowns
        self.time = time
        self.went = False
    def __str__(self):
        return str(self.crowns) + " " + str(self.time)
def printList(people):
    for p in people:
        print(p)
persons, time = input().split()
time = int(time)
persons = int(persons)
people = []

for x in range(persons):
    info = input().split()
    people.append(Person(int(info[0]),int(info[1])))


banks  = []
for t in range(max(x.time for x in people)+1):
    banks.append(Person(0,t))

people.sort(key = lambda x: -1*x.crowns)

for p in people:
    for x in range(len(banks)-1, -1, -1):
        if not p.went and p.time>=x and p.crowns>banks[x].crowns:
            banks[x] = p
            p.went = True
            break
s = 0
for p in banks:
    s+=p.crowns
print(s)
