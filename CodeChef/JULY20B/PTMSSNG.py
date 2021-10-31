t = int(input())
while(t != 0):
  t -= 1
  n = int(input())
  n = (4*n) - 1
  ax = {}
  ay = {}
  px = 0
  py = 0
  while(n != 0):
    n -= 1
    x,y = list(map(int,input().split()))
    px = ax.get(x)
    py = ay.get(y)
    if(px):
      ax.pop(x)
    else:
      ax.update({x:1})
    if(py):
      ay.pop(y)
    else:
      ay.update({y:1})
  for key in ax:
    px = key
  for key in ay:
    py = key
  print(px,py)