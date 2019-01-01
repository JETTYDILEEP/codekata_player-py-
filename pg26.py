def main():
  n=input()
  n=list(n)
  t=[]
  for i in range(len(n)):
    if(i!=' '):
      t.append(n[i])
  l=''.join(t)      
  
  print(l)
main()
