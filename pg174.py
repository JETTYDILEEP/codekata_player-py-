m=input()
n=input()
t,l=[],[]
c=0
if (m.isalpha() or " " in m) and (n.isalpha() or " " in n):
    m=list(m.split(" "))
    n=list(n.split(" "))
    for i in m:
        if m.count(i) > n.count(i) and i not in l:
            c=c+1
            t.append(c)
            l.append(i)
    for i in n:
        if n.count(i)>m.count(i) and i not in l:
            c=c+1
            t.append(c)
            l.append(i)

else:
    for i in m:
        if m.count(i)>n.count(i) and i not in l:
            c=c+1
            t.append(c)
            l.append(i)
    for i in n:
        if n.count(i)>m.count(i) and i not in l:
            c=c+1
            t.append(c)
            l.append(i)
for i in range(len(t)):
    print(t[i],':',l[i])
