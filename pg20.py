def main():
  s=str(input())
  l=[]
  for i in s:
    n=ord(i)+3
    str=chr(n)
    l.append(str)
  print(''.join(l))  

main()
