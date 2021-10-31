a = [2,3,1]
i = 4
while(i <= 100000):
    if(not (i & (i-1))):
        a.append(i+1)
        a.append(i)
        i += 1
    else:
        a.append(i)
    i += 1
for _ in range(int(input())):
    n = int(input())
    if(n == 1):
        print("1")
        continue
    if(not (n & (n-1))):
        print("-1");
        continue
    for i in range(n):
        print(a[i],end=" ")
    print()