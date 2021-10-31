import sys
table = []
def subset_sum(numbers, target, partial=[], psum=0):
    if (psum == target and len(partial)>1):
        table.append(partial)
    if (psum >= target and len(partial)>1):
        table.append(partial)
        return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n], psum+n)

def subset_sum2(numbers, target1, target2, partial=[], psum=0):
    if psum >= target1 and psum <= target2:
        return True

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        check = subset_sum2(remaining, target1, target2, partial + [n], psum+n)
        if(check == True):
            return True

for _ in range(int(input())):
    n,k = map(int,input().split())    
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    c1 = 0
    c2 = 0
    sum1 = 0
    sum2 = 0
    tsum = sys.maxsize
    subset_sum(a,k*2)
    for t in table:
        lent = len(t)
        if(lent >= tsum):
            continue
        checker = subset_sum2(t,k,sum(t)-k)
        if(checker == True):
            if(lent < tsum):
                tsum = lent
    if(len(a) == 1 or tsum > 4000):
        print(-1)
    else:
        print(tsum)
    table = []