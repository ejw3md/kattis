class thing:
        def __init__(self, y, name):
                self.y = y
                self.name = name


score = int(input())
possible = []
for x in range(1, 21):
	possible.append(thing(x, "single "+str(x)))
	possible.append(thing(2*x, "double "+str(x)))
	possible.append(thing(3*x, "triple " + str(x)))
possible.sort(key=lambda x: x.y, reverse=True)
i = 0
count = 0
ans=""

while(score !=0 and count<=2):
    i=0
    while(i!=len(possible)):
        if(count==0):
            if(score>=possible[i].y and score-possible[i].y>=0 and (score-possible[i].y)%2==0):
                score-=possible[i].y
                ans+=possible[i].name + "\n"
                break
            else:
                i+=1
        elif(score>=possible[i].y and score-possible[i].y>=0):
            score-=possible[i].y
            ans+=possible[i].name + "\n"
            break
        else:
            i+=1
    count+=1

if(score==0):
    print(ans)
else:
    print("impossible")
