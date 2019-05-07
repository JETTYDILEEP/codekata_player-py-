class pg199:
    def func(n):
        for i in n:
            if(n.count(i)>1):
                print('yes')
                break
        else:
            print('no')
            
        
n=str(input())
pg199.func(n)
