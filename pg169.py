class pg169:
    def func(n):
        n=list(n)
        b=[]
        for i in range(0,len(n)):
          if(n[i] not in b):
            b.append(n[i])
            b.append(n.count(n[i]))
        
        
        print(*b,sep='')
            
n=input()
pg169.func(n)
