n=int(input())
l=[int(x) for x in input().split()]
c=l.count(0)
m=[]
for i in range(n):
    if l[i]!=0:
        m.append(l[i])
print(m)
for i in range(c):
    m.append(0)
print(*m)
