import sys

mins = sys.maxsize
m = 0
n = 0

def calcMinRoute(a,i,j,ssum):
    global mins,m,n
    ssum += a[i][j]
    if(i == m-1 and j == n-1):
        mins = ssum if (ssum < mins) else mins
    else:
        if (j < n-1):
            calcMinRoute(a,i,j+1,ssum)
        if (i < m-1):
            calcMinRoute(a,i+1,j,ssum)

if __name__ == "__main__":
    m,n = map(int,input().split())
    a = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    calcMinRoute(a,0,0,0)
    print(mins)