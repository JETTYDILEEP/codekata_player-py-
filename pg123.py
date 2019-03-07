m=int(input())
l=[]
f=0
for i in range(2,m//2):
    if m%i==0 :
        for j in range(2,i//2+1):
            if  i%j==0:
                f=1
                break
        if f!=1:
            l.append(i)
        f=0
print(*l,sep=' ')
