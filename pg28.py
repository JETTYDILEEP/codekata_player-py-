def main(l):
  n=list(l)
  a=''
  for i in range(len(n)):
    if (n[i]==' '):
      n[i]=''    
  for i in n:
    a=a+i
  return a    

k=input()

print(main(k))
