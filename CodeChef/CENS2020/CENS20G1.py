from sys import stdin, stdout

t=int(input())
while(t!=0):
  t-=1
  s = list(input())
  x1,y1 = map(int,input().split())
  q = int(input())
  sfreq = {}
  for i in s:
    sfreq[i] = sfreq.get(i, 0) + 1
  while(q!=0):
    q-=1
    x2,y2 = map(int,stdin.readline().split())
    t1 = x2 - x1
    t2 = y2 - y1
    count = 0
    found = 1
    if(t1 > 0):
      if(sfreq.get('R') and sfreq['R'] - t1 >= 0):
        count +=  t1
      else:
        found = 0
    elif(t1 < 0):
      if(sfreq.get('L') and sfreq['L'] + t1 >= 0):
        count -=  t1
      else:
        found = 0
    if(t2 > 0):
      if(sfreq.get('U') and sfreq['U'] - t2 >= 0):
        count +=  t2
      else:
        found = 0
    elif(t2 < 0):
      if(sfreq.get('D') and sfreq['D'] + t2 >= 0):
        count -=  t2
      else:
        found = 0
    if(found == 1):
      stdout.write("YES " + str(count) + '\n')
    else:
      stdout.write("NO" + '\n')