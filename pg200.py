class pg200:
    def func(n):
        l=[]
        for i in n:
            if(n.count(i)>=1 and i not in l):
                l.append(i)    
        print(*l,sep='')
n=str(input())
pg200.func(n)
