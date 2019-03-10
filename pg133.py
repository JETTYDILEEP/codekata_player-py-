m,n=map(int,input().split())
l=[]
c=0
for i in range(0,m):
    l.append(list(map(int,input().split())))
for i in range(0,len(l)):
    if l[i][1]==n:
        c=c+1
if c==0:
    print("no")
else:
    print("yes")
