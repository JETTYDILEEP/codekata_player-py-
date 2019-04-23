class pg155:
    def func(n,c):
        l=[int(x) for x in input().split()]
        li1,li2=[],[]
        for i in range(0,c):
            li1.append(l[i])
        for i in range(c,n):
            li2.append(l[i])
        
        li1.sort()
        li2.sort()
        li2.reverse()
        li=[]
        for i in range(len(li1)):
            li.append(li1[i])
        for i in range(len(li2)):
            li.append(li2[i])
        print(*li,sep=' ')

n,c=map(int,input().split())
pg155.func(n,c)
