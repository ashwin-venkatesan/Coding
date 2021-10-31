def maxSubarray(arr, n, m):
    x = 0
    prefix = 1
    maxim = 0
    S = set()
    for i in range(n):
        prefix = (prefix * arr[i])
        if(prefix%m > maxim %m):
            maxim = prefix
        it  = 0
        S.add(arr[i])
        for j in S:
            if((prefix//j)%m > prefix%m):
                if(it != 0):
                    if(((prefix//j)%m > (prefix//it)%m)):
                        it = j
                else:
                    it = j
        if(it != 0):
            prefix = prefix//it
            maxim = prefix
        S.pop()
        S.add(prefix)
    return (maxim%m)

for _ in range(int(input())):
    n,m = map(int,input().split())
    g = list(map(int,input().split()))
    l = list(map(int,input().split()))
    lg = list(map(int,input().split()))
    groups = {}
    for i in range(n):
        if(not groups.get(g[i])):
            groups[g[i]] = []
        groups[g[i]].append(l[i])
    for ky,val in groups.items():
        print(maxSubarray(val,len(val),lg[ky-1]),end=' ')
    print()
