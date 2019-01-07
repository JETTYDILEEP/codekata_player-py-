def main(l):
  n=' '
  for i in l:
    if(i.isupper()):
      n=n+i.lower()
      
    elif(i.islower()):
      n=n+i.upper()
  return n    

k=input()

print(main(k))
