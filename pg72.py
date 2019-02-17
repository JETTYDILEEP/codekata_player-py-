class Bitonic:
  def ope(N,l):
    for i in range(0,N-1):
      if(l[i]>l[i+1]and l[i]>l[i-1]):
        print(l[i])
      else:
        continue 
    

N=int(input())
l=list(input().split())
if(N==len(l)):
  Bitonic.ope(N,l)
