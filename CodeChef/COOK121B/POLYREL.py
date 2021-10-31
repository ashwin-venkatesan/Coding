t=int(input())
while(t!=0):
    t-=1
    n = int(input())
    temp = n
    while(temp!=0):
        x,y = map(int,input().split())
        temp -= 1
    temp = n
    if(temp%2 == 1):
        temp-=1
    sum = n
    while(temp > 5):
        if(temp%2 == 1):
            sum +=(temp-1)//2
        else:
            sum += temp//2
        temp //= 2
    print(sum)