m,n=input().split(' ')
c=0
for i in range(len(m)):
    if m[i]!=n[i]:
        c=c+1
if(c==1):print('yes')
else:print('no')
