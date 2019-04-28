class pg176:
    def func(m,n):
        m=list(m)
        n=list(n)
        c=0
        for i in range(len(n)):
            if(n[i] not in m):
                c=c+1
        if(c>=1):
            print('false')
        else:
            print('true')
m,n=map(str,input().split())
pg176.func(m,n)
