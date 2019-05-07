class pg196:
    def func(n,l):
        for i in range(0,n):
            if(l.count(l[i])==1):
                print(l[i])
            
        
n=int(input())
l=[int(x) for x in input().split()]
pg196.func(n,l)
