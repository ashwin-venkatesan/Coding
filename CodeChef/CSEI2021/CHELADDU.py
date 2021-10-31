for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    mindiff = 1000000000
    a.sort()
    for i in range(len(a)-k+1):
        mindiff = min(mindiff, a[i+k-1]-a[i])
    print(mindiff)