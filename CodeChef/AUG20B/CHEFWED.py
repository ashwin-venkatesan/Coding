from array import *

def arrcost(arr):
    freq = {}
    sum = 0
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    for i in freq:
        if(not freq[i] == 1):
            sum += freq[i]
    return sum

t = int(input())
while(t!=0):
    t -= 1
    n,k = map(int, input().split())
    f = list(map(int, input().split()))
    dpcost = [[0 for i in range(n)] for j in range(n)] 
    for i in range(n):
        freq = {}
        for j in range(i,n):
            freq[f[j]] = freq.get(f[j], 0) + 1
            if(freq[f[j]] == 2):
                dpcost[i][j] += dpcost[i][j-1] + 2
            elif(freq[f[j]] > 2):
                dpcost[i][j] += dpcost[i][j-1] + 1
            else:
                dpcost[i][j] += dpcost[i][j-1]
    total=[0]*n
    for i in range(n):
        temp=dpcost[0][i]
        for j in range(i):
            temp=min(temp,total[j]+dpcost[j+1][i])
        total[i]=temp+k
    print(total[n-1]) 