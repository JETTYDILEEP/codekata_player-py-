m=int(input())
li=[]
for i in range(m):
  lis=list(map(int,input().split()))
  li.append(lis)
a=0;b=0
k=m-1
for i in range(m):
  a+=li[i][i]
  b+=li[i][k]
  k-=1
print(a*b)
