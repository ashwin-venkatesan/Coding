t = int(input())
while(t != 0):
    t-=1
    input()
    c = int(input())
    n = int(input())
    totsum = 0
    cursum = 0
    curcap = 0
    cursum = 0
    x = 0
    y = 0
    for i in range(n):
        a = list(map(int,input().split()))
        if(curcap+a[2] > c):
            totsum += cursum + x + y
            curcap = 0
            cursum = 0
            x = 0
            y = 0
        curcap += a[2]
        cursum += abs(a[0]-x) + abs(a[1]-y)
        x = a[0]
        y = a[1]
    totsum += cursum + x + y
    print(totsum)
    if(t != 0):
        print()