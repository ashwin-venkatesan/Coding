# Question 1: Given a string A consisting of n characters and a string B consisting of m characters, write a function that will return the number of times A must be stated such that B is a substring of the repeated A. If B can never be a substring, return -1.

# Example:
# A = ‘abcd’
# B = ‘cdabcdab’
# The function should return 3 because after stating A 3 times, getting ‘abcdabcdabcd’, B is now a substring of A.

# You can assume that n and m are integers in the range [1, 1000].
a='abcd'
b='cdabcdabcdabcdab'
ptr=-1
for i in range(len(a)):
    if b.startswith(a[i:]):
        ptr=i
        break
if ptr==-1:
    print(-1)
else:
    blen=len(b)
    alen=len(a)
    aptr=0
    bptr=(alen-ptr)
    count=1
    while bptr<blen:
        if aptr==0:
            count+=1
        if a[aptr]!=b[bptr]:
            aptr=-1
            bptr=-1
            break
        aptr=(aptr+1)%alen
        bptr+=1
    if aptr==-1:
        print(-1)
    else:
        print(count)