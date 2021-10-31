import math 

def maximumXOR(n, l, r): 
    x = 0
    for i in range(int(math.log2(r)), -1, -1):  
        if (n & (1 << i)): # Set bit  
            if (x > r) or (x + (1 << i) - 1 < l): 
                x ^= (1 << i) 
        else: # Unset bit 
            if (x ^ (1 << i)) <= r: 
                x ^= (1 << i) 
    return n ^ x 
  
# Driver code 
n = 7
l = 2
r = 23
print("The output is",  
       maximumXOR(n, l, r)) 
