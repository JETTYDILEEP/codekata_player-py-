class pg187:
    def func(m,n):
        l=len(m)
        k=len(n)
        a,b,c=[],[],[]
        for i in range(1, l + 1):
            if l % i == 0:
               a.append(i)
        for i in range(1, k + 1):
            if k % i == 0:
               b.append(i)
        
        a=set(a)
        b=set(b)
        c=(a&b)
        if(len(c)==1):
            print('yes')
        else:
            print('no')

m,n=map(str,input().split())
pg187.func(m,n)
