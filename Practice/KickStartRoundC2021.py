count = 0

def palgen(curword,k,n,s):
    global count
    if(len(curword)<n):
        for j in range(k):
            curword += chr(97+j)
            # print(curword)
            palgen(curword,k,n,s)
            curword = curword[0:len(curword)-1]
    else:
        if(len(curword) == n and curword == curword[::-1] and curword < s):
            count+=1

tc = int(input())
for _ in range(1, tc + 1):
    n,k = map(int,input().split())
    s = input()
    ans = palgen('',k,n,s)
    print("Case #{}: {}".format(_,count))