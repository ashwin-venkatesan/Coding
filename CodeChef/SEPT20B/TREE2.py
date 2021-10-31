for _ in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  freq = {}
  for i in a:
    freq[i] = freq.get(i,1)
  if(len(freq)==1 and freq.get(0,-1)!=-1):
    print("0")
  elif(freq.get(0,-1)!=-1):
    print(len(freq)-1)
  else:
    print(len(freq))