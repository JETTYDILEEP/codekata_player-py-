n=input()
x,y=[],[]
for i in n:
	x.append(n.count(i))
m=max(x)
for i in n:
	if n.count(i)==m:
		if i not in y:
			y.append(i)
print(m,end=" ")
for i in y:
	print(i,end="")
