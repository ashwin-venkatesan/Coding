m=int(input())
while(m):
    s=input()
    freq={}
    n=int(input())
    for i in s:
        freq[i] = freq.get(i, 0) + 1      
    max_prod=0
    max_woman=0
    prod=1
    points=[]
    k=0
    while(n):
        print(freq)
        prod=1
        woman=input()
        copy_freq = freq.copy()
        for i in woman:
            if(copy_freq.get(i,-1) <= 0):
                prod = 0
                print(i)
            else:
                prod=prod*freq.get(i,0)
            if(prod==0):
                break
            copy_freq[i] -= 1
        if(prod==0):
            print(prod)
            n=n-1
            continue
        if(prod>max_prod):
            max_prod=prod
            max_woman=woman
        print(prod)
        n=n-1

    if(max_prod!=0):
        print(max_woman)
    else:
        print("No Research This Month")
    m=m-1