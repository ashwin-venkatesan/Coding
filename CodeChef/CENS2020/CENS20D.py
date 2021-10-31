t = int(input())
while(t!=0):
  t-=1
  n=int(input())
  a = list(map(int,input().split()))
  lena = len(a)
  total = 0
  for i in range(len(a)-1):
    for j in range(i+1,len(a)):
      if(a[i] == a[i] & a[j]):
        total+=1
  print(total)