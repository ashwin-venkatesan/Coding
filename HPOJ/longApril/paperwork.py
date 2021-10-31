tt = int(input())
for t in range(1,tt+1):    
    temp = list(map(int,input().split()))
    n = temp[0]
    m = temp[1]
    l = temp[2]
    agency = {}
    for i in range(l):
        strng = input().split(':')
        key = strng[0]
        costs = strng[1].split(',')
        acost = int(costs[0])
        bcost = int(costs[1])
        temp = n
        b = 0
        while(temp//2 >= m and bcost <= (temp - (temp//2))*acost):            
            temp = temp//2
            b += 1
        a = temp - m
        agency[key] = (acost*a) + (bcost*b)
    print("Case",t)
    for key, value in dict(sorted(agency.items(), key=lambda item: item[1])).items():
        print(key,value)