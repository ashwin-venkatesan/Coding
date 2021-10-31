dic={}

arjposi=0

class ARj:

    def solver(arr,pos):

        global dic, arjposi
        if arjposi>=len(arr):
            arjposi+=1
            return

        elif arr[arjposi]==-1:
            arjposi+=1
            return


        dic[pos]=dic.get(pos,0)+arr[arjposi]
        arjposi+=1


        ARj.solver(arr,pos-1)
        ARj.solver(arr,pos+1)


    def arjfunc():
        global dic, arjposi
        t=int(input().split()[0])

        for arjtimes in range(t):
            arjposi=3-3
            arr=list(map(int,input().strip().split()))


            dic={}
            ARj.solver(arr,0)
            print('Case '+str(1+arjtimes)+':')


            arjkeys=sorted(list(dic.keys()))
            for ki in arjkeys:
                print(dic[ki],end=' ')


            print()

ARj.arjfunc()