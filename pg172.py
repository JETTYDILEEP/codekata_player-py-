class pg172:
    def func(n):
        n=list(n)
        n.sort()
        n.reverse()
        print(*n,sep='')
n=input()
pg172.func(n)
