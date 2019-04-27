s=input()
x,y=[],[]
for i in s:
	x.append(s.count(i))
m=max(x)
for i in s:
	if s.count(i)==m:
		if i not in y:
			y.append(i)
print(m,end=" ")
for i in y:
	print(i,end="")
