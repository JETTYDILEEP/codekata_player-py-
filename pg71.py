class consecutive:
  def ope(N,l):
    l1=[]
    for i in range(0,N-1):
      if(l[i]>l[i+1]):
        l1.append(l[i])
      else:
        l1.append(l[i+1])  
    l1=' '.join(l1)
    print(l1)

N=int(input())
l=list(input().split())
if(N==len(l)):
  consecutive.ope(N,l)
