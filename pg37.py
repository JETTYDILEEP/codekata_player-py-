n=int(input())
i=[]
j=[]
for m in range(n):
  a,b=map(int,input().split())
  i.append(a)
  j.append(b)
if(n < 6):
  print(n-1)  
else:
  print(n-2)
