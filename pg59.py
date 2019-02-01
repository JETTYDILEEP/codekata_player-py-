n1=int(input())
l=input()
if(n1==len(l)):
  l=l[0:l.rindex('0')]
  print(*list(x for x in l if x=='1'))
