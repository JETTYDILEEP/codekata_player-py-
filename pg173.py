m=input()
n=input()
l=[]
if (m.isalpha() or " " in m) and (n.isalpha() or " " in n):
    m=list(m.split(" "))
    n=list(n.split(" "))
    for i in m:
        if m.count(i) > n.count(i) and i not in l:
            l.append(i)
    for i in n:
        if n.count(i)>m.count(i) and i not in l:
            l.append(i)
    print(*l)
else:
    for i in m:
        if m.count(i)>n.count(i) and i not in l:
            l.append(i)
    for i in n:
        if n.count(i)>m.count(i) and i not in l:
            l.append(i)
    print(*l)
