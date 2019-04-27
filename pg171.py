class pg171:
    def func(n):
        n=list(n.split(' '))
        for i in range(len(n)):
            if(n[i]=='and'and len(n)>1):
                n[i-1],n[i+1]=n[i+1],n[i-1]
        print(*n,sep=' ')
n=str(input())
pg171.func(n)
