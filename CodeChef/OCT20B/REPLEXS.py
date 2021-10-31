for _ in range(int(input())):
    n, x, p, k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if(a[p-1] == x):
        print("0")
        continue
    if(k > p):
        if(a[p-1] < x):
            print("-1")
        else:
            i = 0
            while(a[i] <= x):
                i += 1
            print(p-i)
    elif(k < p):
        if(a[p-1] > x):
            print("-1")
        else:
            i = n-1
            while(a[i] >= x):
                i -= 1
            print(i-p+2)
    else:
        if(a[p-1] > x):
            i = 0
            while(a[i] <= x):
                i += 1
            print(p-i)
        else:
            i = n-1
            while(a[i] >= x):
                i -= 1
            print(i-p+2)