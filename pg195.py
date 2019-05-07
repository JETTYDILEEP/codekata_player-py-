class pg195:
    def func(n,x):
        while(n>x):
            n=n-x
        print(n)
        
n,x=map(int,input().split())
pg195.func(n,x)
