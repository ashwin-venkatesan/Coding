t=int(input())
while(t!=0):
  t-=1
  s = list(input())
  x1,y1 = map(int,input().split())
  q = int(input())
  while(q!=0):
    q-=1
    x2,y2 = map(int,input().split())
    t1 = x1
    t2 = y1
    count = 0
    found = 0
    for i in s:
      if(x2<t1 and y2<t2):
        if(i == 'L'):
          t1 -= 1
          count += 1
        elif(i == 'U'):
          t2 -= 1
          count += 1
      elif(x2>t1 and y2<t2):
        if(i == 'R'):
          t1 += 1
          count += 1
        elif(i == 'U'):
          t2 -= 1
          count += 1
      elif(x2>t1 and y2>t2):
        if(i == 'R'):
          t1 += 1
          count += 1
        elif(i == 'D'):
          t2 += 1
          count += 1
      elif(x2<t1 and y2>t2):
        if(i == 'L'):
          t1 -= 1
          count += 1
        elif(i == 'D'):
          t2 += 1
          count += 1
      elif(x2 == t1 and y2<t2):
        if(i == 'U'):
          t2 -= 1
          count += 1
      elif(x2 == t1 and y2>t2):
        if(i == 'D'):
          t2 += 1
          count += 1
      elif(y2 == t2 and x2<t1):
        if(i == 'L'):
          t1 -= 1
          count += 1
      elif(y2 == t2 and x2>t1):
        if(i == 'R'):
          t1 += 1
          count += 1
      else:
        found = 1
        break
    if(found == 1):
      print("YES",count)
    else:
      print("NO")