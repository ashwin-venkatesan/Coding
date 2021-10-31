t = int(input())
while (t!=0):
    t -= 1
    s = list(input())
    p = list(input())
    for i in range(len(p)):
        if(i==0):
            continue
        s.remove(p[i])
    s.sort()
    f = p[0]
    p.pop(0)
    i = 0
    while(p[i] == f and i < len(p)):
        i += 1
    fn = p[i]
    p = ''.join(p)
    s = ''.join(s)
    if(fn >= f):
        pf = s.rfind(f)
    else:
        pf = s.find(f)
    s = list(s)
    s.insert(pf + 1,p)
    s = ''.join(s)
    print(s)