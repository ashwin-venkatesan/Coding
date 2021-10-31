t=int(input())
while(t!=0):
    t-=1
    n,k = map(int,input().split())
    a = list(map(int,input()))
    div = n // k
    freq = {}
    count0 = 0
    count1 = 0
    for i in a:
        freq[i] = freq.get(i, 0) + 1
    if(freq.get(0,-1) == -1):
        count0 = 0
    else:
        if(not freq[0] % div == 0):
            print("IMPOSSIBLE")
            continue
        count0 = freq[0] // div
    if(freq.get(1,-1) == -1):
        count1 = 0
    else:
        if(not freq[1] % div == 0):
            print("IMPOSSIBLE")
            continue
        count1 = freq[1] // div
    strng = []
    for i in range(count0):
        strng.append('0')
    for i in range(count1):
        strng.append('1')
    strng = "".join(strng)
    for i in range(div):
        if(i%2 == 0):
            print(strng,end="")
        else:
            print(strng[::-1],end="")
    print()