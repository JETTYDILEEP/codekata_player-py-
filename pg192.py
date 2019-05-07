n=int(input())
l=[int(x) for x in input().split()]
c=1
k=-1
for i in range(0,n-1):
    if(l[i]<l[i+1]):
       c=c+1
    else:
        k=k-1
        
if(c+k==0):
    print('yes')
else:
    print('no')
        

