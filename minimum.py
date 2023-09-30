def mincost() :
    t=int(input())
    l=[]
    while t>0 :
        n=int(input())
        for i in range(n):
            num = input()
            num=num.split()
            l.append(num)
        k=int(input())
        c=int(input())
        leng=len(l)
        cost = k*leng
        print(cost)
        t-=1
mincost()
