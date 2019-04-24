n,m=map(int,input().split())
v=bin(n*m)
c,p=0,1
for x in range(2,len(v)):
    c=c+1
    if(v[x]=='1'):
        if(p==2):
            print(c)
            break
        p=p+1
