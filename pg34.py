def func(n):
  t=''
  for i in range(0,len(n),3):
    t=t+n[i]
  return t

s=str(input())
print(func(s))
