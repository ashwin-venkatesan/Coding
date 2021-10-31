t = int(input())
while(t!=0):
	t -= 1
	n,m = map(int,input().split())
	t1 = { 0 }
	s = [0]
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	while(len(s) > 0):
		e1 = s.pop()
		for i in a:
			e2 = i
			if(not (e1|e2) in t1):
				t1.add(e1|e2)
				s.append(e1|e2)
		for i in b:
			e2 = i
			if(not (e1&e2) in t1):
				t1.add(e1&e2)
				s.append(e1&e2)
	print(len(t1))