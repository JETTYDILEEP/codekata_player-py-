n=int(input())
val=''
num=input()
num=num.replace('0','')
val+=num[:len(num)-1]
print(val)
