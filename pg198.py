vclass pg198:
    def func(n,l):
        print(l.index(max(l))-l.index(min(l)))
            
        
n=int(input())
l=[int(x) for x in input().split()]
pg198.func(n,l)
