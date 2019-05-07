class pg194:
    def func(a,b):
        if(a=='R' and b=='P'):
            print(b)
        elif(a=='S' and b=='P'):
            print(a)
        elif(a=='R' and b=='S'):
            print(a)
a,b=map(str,input().split())
pg194.func(a,b)
