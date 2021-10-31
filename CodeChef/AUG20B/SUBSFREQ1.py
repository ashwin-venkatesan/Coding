t = int(input())
while(t!=0):
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    o = [0] * n
    o[0] = 1
    m = 1000000007
    for i in range(1,n):
        o[i] = (o[i-1]*2) % m
    for i in range(n-1,-1,-1):
        print(o[i], end=" ")
    print()
