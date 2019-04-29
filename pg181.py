class pg181:
    def func(n):
        c=0
        for i in range(1,n+1):
            if(n%3==0 and c<n):
                c=c+3
            elif(n%7==0 and c<n):
                c=c+7
        if(c==n):
            print('yes')
        else:
            print('no')
n=int(input())
pg181.func(n)
