n=int(input())
arr=[int(x) for x in input().split()]
if(len(arr)==n):
  if(arr==sorted(arr)):
    print('yes')
  else:
    print('no')
