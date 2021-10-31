t=int(input())
while(t!=0):
    t-=1
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    sum = 0
    flag = 0
    count = 1
    for i in a:
        if(i > k):
            flag = 1
            break
        if(i+sum > k): 
            sum = 0
            count+=1
        sum += i
    if(flag == 1):
        print("-1")
    else:
        print(count)