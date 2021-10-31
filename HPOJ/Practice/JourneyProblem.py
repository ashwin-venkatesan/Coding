import sys
import math

def findy(x1,y1,x2,y2,x):
    return ( (((y2-y1)/(x2-x1))*(x-x1))+y1 )

def dist(x1,y1,x2,y2):
    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

for _ in range(int(input())):
    n = int(input())
    graph = {}
    maxx = -sys.maxsize - 1
    minx = sys.maxsize
    miny = 0
    maxy = 0
    total = 0
    for i in range(n):
        x,y = map(int,input().split())
        graph[x] = y
        if(x > maxx):
            maxx = x
            maxy = y
        if(x < minx):
            minx = x
            miny = y
    curpx = minx
    curpy = miny
    for x in sorted(graph.keys()):
        if(x == minx):
            continue
        y = graph[x]
        yline = findy(minx,miny,maxx,maxy,x)
        prevxb = minx
        prevyb = miny
        nextxa = maxx
        nextya = maxy
        nextxb = maxx
        nextyb = maxy
        flag = 0
        for tempx in sorted(graph.keys()):
            if(flag == 0):
                if(tempx != x):
                    prevx = tempx
                    prevy = graph[tempx]
                elif(tempx == x):
                    flag = 1
            else:
                nextx = tempx
                nexty = graph[tempx]
                if(flag == 1):
                    nextyline = findy(minx,miny,maxx,maxy,nextx)
                    if(nexty >= nextyline):
                        nextxa = nextx
                        nextya = nexty
                        flag = 2
                    else:
                        nextxb = nextx
                        nextyb = nexty
                        flag = 3
                elif(flag == 2):
                    nextyline = findy(minx,miny,maxx,maxy,nextx)
                    if(nexty < nextyline):
                        nextxb = nextx
                        nextyb = nexty
                        break
                elif(flag == 3):
                    nextyline = findy(minx,miny,maxx,maxy,nextx)
                    if(nexty >= nextyline):
                        nextxa = nextx
                        nextya = nexty
                        break
        al = dist(curpx,curpy,x,y)
        ar = dist(x,y,nextxa,nextya)
        bl = dist(prevxb,prevyb,x,y)
        br = dist(x,y,nextxb,nextyb)
        if(al + ar <= bl + br):
            total += dist(curpx,curpy,x,y)
            curpx = x
            curpy = y
            print("tr",x,y)
            del graph[x]

    for x in sorted(graph.keys(),reverse=True):
        total += dist(curpx,curpy,x,graph[x])
        curpx = x
        curpy = graph[x]
        del graph[x]        
    
    print(round(total,2))