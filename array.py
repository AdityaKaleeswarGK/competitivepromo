import math 
def arr():
    t=int(input())
    while t>0 :
        n=int(input())
        print(math.ceil(math.log2(n)))
        t-=1
    
arr()
