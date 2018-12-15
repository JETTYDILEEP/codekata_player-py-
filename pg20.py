def main():
  s=str(input())
  l=[]
  for i in s:
    n=ord(i)+3
    st=chr(n)
    l.append(st)
  print(''.join(l))  

main()
