def secsmall(list,m):
  if(len(list)==m):
    list.sort()
    print(list[1])

m=int(input())
list=[int(x) for x in input().split()]
secsmall(list,m)
