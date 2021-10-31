for _ in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  n -= 1
  while(n!=0):
    n-=1
    b = list(map(int,input().split()))
  count = 0
  i = len(a)-1
  flag = 0
  count = 0
  while(i!=0):
    if(flag == 0 and a[i] != i+1):
      flag = 1
      count += 1
    elif(flag == 1 and a[i] == i+1):
      count += 1
      flag = 0
    i-=1
  print(count)