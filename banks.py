from typing import List, Tuple
from collections import namedtuple

Person = namedtuple("Person", ["crowns", "time"])

def make_test_case() -> Tuple[List[Person], int]:
    from random import randint
    N = randint(1, 10000)
    T = randint(1, 47)
    people = [Person(randint(1, 100000), randint(0, T-1)) for _ in range(N)]
    return people, T

def bank(people: List[Person], closing: int) -> int:
    a: List[List[Person]] = [[] for _ in range(closing)]
    for p in people:
        a[p.time].append(p)
    for i in range(closing):
        a[i].sort(reverse=True, key=lambda p: p.crowns)
        #del a[i][i+1:]
        # if there are more than i+1 that will leave after t_i
        # then we can at best only serve the highest paying i+1
    used: List[Tuple[int, Person]] = []
    for t in range(closing)[::-1]:
        if a[t]:
            used.append((t, a[t][0]))
            del a[t][0]
            if t > 0:
                a[t-1] += a[t]
                a[t-1].sort(reverse=True, key=lambda p: p.crowns)
    return sum(p[1].crowns for p in used)

if __name__ == "__main__":
    import sys
    N, T = [int(s) for s in sys.stdin.readline().split()]
    people = [Person(*[int(s) for s in line.split()]) for line in sys.stdin]
    print(bank(people, T))
