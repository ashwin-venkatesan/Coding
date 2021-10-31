from itertools import combinations

t = int(input())
while(t!=0):
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    subsets = sum([list(map(list, combinations(a, i))) for i in range(1,len(a) + 1)], [])
    paper = []
    dpmap = {}
    dpfreq = {}
    kys = 1
    for subset in subsets:
        found = 0
        for key, value in dpmap.items(): 
            if subset == value: 
                paper.append(dpfreq[key])
                found = 1
                break
        if(found):
            continue
        freq = {}
        for i in subset:
            freq[i] = freq.get(i, 0) + 1
        temp = max(freq.values())
        tempkeys = []
        for key, value in freq.items(): 
            if temp == value: 
                tempkeys.append(key)
        temp2 = min(tempkeys)
        dpmap[kys] = subset
        dpfreq[kys] = temp2
        kys += 1
        paper.append(temp2)
    print(paper)
    freq = {}
    for i in paper:
        freq[i] = freq.get(i, 0) + 1
    for x in range(1,n+1):
        print(freq.get(x, 0), end=" ")
    print()