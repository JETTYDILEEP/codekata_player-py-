import math
try:
    v = int(input())
    c=0
    a=[]
    while(v%2==0):
        v = int(n/2)
        c+=1
    if(c>0):
        c=0
        print(2,end= " ")
    for i in range(3,int(math.sqrt(v))+1,2):
        while(v%i==0):
            v=int(v/i)
            c+=1
        if(c>0):
            c=0
            print(i,end= " ")
    if v>2:
        print(v,end=" ")    
except:
    print("Invalid Input")
