def who_lost(i, lost):
    lost = True
    if i % 2 == 0:
       print("Player 2 lost")
    else:
       print("Player 1 lost")
    return True
s = set()
lost = False
words = int(input())
i = 0
first = input()
prev_letter = first[-1]
s.add(first)
for _ in range(words-1):
    word = input()
    if word in s or word[0]!= prev_letter:
        lost = who_lost(i, lost)
        break
    prev_letter = word[-1]
    i+=1
    s.add(word)
if not lost:
    print("Fair Game")