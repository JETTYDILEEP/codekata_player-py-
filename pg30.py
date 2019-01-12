l=input().split()
n=int(l[2])
c=0
a=l[0]
b=l[1]
for x in range(0,len(a)):
    if(a[x]!=b[x]):
        c=c+1
if(c==n):
    print("yes")
else:
    print("no")
