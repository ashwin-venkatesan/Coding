for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    odsum = 0
    evsum = 0
    for i in range(0,len(a),2):
        evsum += a[i]
    for i in range(1,len(a),2):
        odsum += a[i]
    print(max(odsum, evsum))