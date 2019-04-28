m,n=map(int,input().split())
p=m^n
d=bin(p)
c=d.count("1")
print(c)
