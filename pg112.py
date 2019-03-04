class pg112:
  def func(n,l): 
    s=[]
    if(n==len(l)):
      for i in range(n+1): 
        for j in range(i+1,n+1): 
          sub=l[i:j] 
          #print(sub)
          s.append(sub) 
              

      return len(s)
  
n=int(input())
l=[int(x) for x in input().split()] 
print(pg112.func(n,l)) 
