class pg196:
    def func(n,l):
        c=0
        for i in range(0,n-1):
            if(l.count(l[i])<l.count(l[i+1])):
                c=l[i]
            
        print(c)
n=int(input())
l=[int(x) for x in input().split()]
pg196.func(n,l)
