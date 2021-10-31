for _ in range(int(input())):
    n,m = map(int,input().split())    
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    suma = sum(a)
    sumb = sum(b)
    vc = 0
    if(suma > sumb):
        print(vc)
        continue
    a.sort()
    b.sort()
    i = 0
    j = m - 1
    flag = 0
    while(i < n and j >= 0 and a[i] < b[j]):
        suma -= a[i]
        sumb -= b[j]
        suma += b[j]
        sumb += a[i]
        vc += 1
        i += 1
        j -= 1
        if(suma > sumb):
            flag = 1
            break
    if(flag):
        print(vc)
    else:
        print(-1)