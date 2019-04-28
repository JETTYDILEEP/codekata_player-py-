m=input()
n=input()
l=m+n
for i in l:
    if l.count(i)!=1 or len(l)<26:
        print("non-complementary")
        break
    else:
        print("complementary")
        break
