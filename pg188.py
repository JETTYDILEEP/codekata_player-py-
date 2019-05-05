class pg188:
    def func(a,b,c):
        if(a<(b+c)):
            if(b<(a+c)):
                if(c<(a+b)):
                    print('yes')
                else:
                    print('no')
            else:
                print('no')
        else:
            print('no')
m,n,o=map(int,input().split())
pg188.func(m,n,o)
