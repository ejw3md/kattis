from math import sqrt
l = []
l.append(sqrt(2))
for x in range(100):
	s=0
	for y in l:
		s+=y
	l.append(sqrt(s))
	print(sqrt(s))
	
		