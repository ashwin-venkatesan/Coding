# cook your dish here
t = int(input())
while(t!=0):
    t-=1
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    x=0
    y=0
    x+=a[0]
    y+=a[1]
    y+=a[2]
    for i in range(3,len(a)):
        if(i%2 == 0):
            y+=a[i]
        else:
            x+=a[i]
    if(x>y):
        print('first')
    elif(y>x):
        print('second')
    else:
        print('draw')