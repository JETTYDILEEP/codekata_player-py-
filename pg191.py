class pg191:
    def func(n,l,m):
        m.reverse()
        if(l==m):
            print('yes')
        else:
            print('no')

a=int(input())
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
pg191.func(a,b,c)
