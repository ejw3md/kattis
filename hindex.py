papers = int(input())
citations = []
for _ in range(papers):
    citations.append(int(input()))
citations.sort(reverse = True)
number = 1
i = 0
while i < len(citations) and number <= citations[i]:
    i+=1
    number+=1
print(number-1)