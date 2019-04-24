n,m=map(int,input().split())
v=bin(n*m)
c=0
for x in range(len(v)-1,1,-1):
    c=c+1
    if(v[x]=='1'):
        print(c)
        break
