import sys

def minDA(a, n, tsum):
    dp = [[0 for i in range(tsum + 1)] 
             for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for j in range(1, tsum + 1):
        dp[0][j] = False
    for i in range(1, n + 1):
        for j in range(1, tsum + 1):
            dp[i][j] = dp[i - 1][j]
            if a[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - a[i - 1]]
    diff = sys.maxsize
    for j in range(tsum // 2, -1, -1):
        if dp[n][j] == True:
            diff = tsum - (2 * j)
            break
    return diff


for _ in range(int(input())):
    n,k = map(int,input().split())    
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    lena = len(a)
    if(lena == 1):
        print(-1)
    tsum = 0
    idk = 0
    while(tsum < 2*k and idk < lena):
        tsum += a[idk]
        idk += 1
    if(idk == 1):
        tsum += a[idk]
        idk += 1
    if(tsum < 2*k):
        print(-1)
        continue
    buf = minDA(a[:idk],idk,tsum)
    buf += (2*k)-tsum
    if(buf <= 0):
        print(idk)
        continue
    bufsum = 0
    while(bufsum < buf and idk < lena):
        bufsum += a[idk]
        idk += 1
    if(bufsum < buf and idk < lena):
        print(-1)
        continue
    print(idk)