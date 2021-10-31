def leafIns(a,i,curpos,l):
    if(a[i] == -1):
        return [i,l]
    l[curpos] = l.get(curpos,0) + a[i]
    temp = leafIns(a,i+1,curpos-1,l)
    i = temp[0]
    l = temp[1]
    temp = leafIns(a,i+1,curpos+1,l)
    i = temp[0]
    l = temp[1]
    if(i+1 == len(a)):
        return [i,l]
    return [i,l]

for t in range(int(input())):
    a = list(map(int,input().split()))
    l = leafIns(a,0,0,{})
    l = l[1]
    print("Case "+str(t+1)+":")
    for i in sorted(l.keys()):
        print(l[i], end=" ")
    print()