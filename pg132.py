n=input()
m=[]
s=0
for i in range(0,len(n)-1):
    k=int(n[i])+int(n[i+1])
    if k%2!=0:
        s=s+1
    else:
        m.append(s)
        s=0
    m.append(s)
    
num=max(m)
if n==0:
    print(0)
else:
    print(num+1)
