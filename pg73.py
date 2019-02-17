class Bitonic:
  def ope(N,l,K):
    for i in range(0,N):
      if(l[i]==K): 
        print(i+1)
        break
      else:
        continue 
    

  

N,K=map(int,(input().split()))
l=[int(x) for x in input().split()]
if(N==len(l)):
  Bitonic.ope(N,l,K)
