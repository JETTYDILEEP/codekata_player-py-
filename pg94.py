n=int(input())
l,c,t=[],1,0
while(n!=0):
  t=n%10
  l.append(t)
  n=n//10
for i in range(0,len(l)):
  if(l.count(l[i])>1):
    c=c+1
    break
if(c>1):
  print('yes')
else:
  print('no')
