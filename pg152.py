n=input()
c=0
l=["a","e","i","o","u"]
for i in range(0,len(n)-2):
    if l.count(n[i])==1 and l.count(n[i+1])==0:
        c=c+2
        if l.count(n[i+1])==0 and l.count(n[i+2])==1:
            c=c+1
print(c)
