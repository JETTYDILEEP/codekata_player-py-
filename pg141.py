n=int(input())
l,c=[],0
for i in range(n):
  l.append(str(input()))
for i in range(n):
  for j in range(n):
    if(l[i]==l[j]):
      c=c+1
if(c>=1):
  print('yes')
else:
  print('no') 
