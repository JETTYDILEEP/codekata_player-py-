class pg202:
    def func(n):
        vow=['a','e','i','o','u']
        m,o='',''
        for i in n:
            if(i in vow):
                m+=i
            else:
                o+=i
        m+=o
        print(m)
n=str(input())
pg202.func(n)
