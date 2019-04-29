class pg182:
    def func(n,l):
        c,v,r=[],[],[]
        for i in range(1,n):
            if(l[i-1]<l[i]):
                c.append(l[i])
                
            elif(l[i-1]==l[i]):
                v.append(l[i+1])
        r.append(c)
        r.append(v)
        print(r.count(min(r))+1)
n=int(input())
l=[int(x) for x in input().split()]
pg182.func(n,l)
