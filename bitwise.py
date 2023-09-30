def arr():
    t = int(input())
    while t>0 :
        n=int(input())
        l = list(map(int, input().split()))
        r = list(map(int, input().split()))
        l1=len(l)
        x=r[0]
        s=r[1]
        check=0
        for i in range(0,l1-1):
            for j in range(i+1,l1) :
                if l[i] ^ l[j]==x and l[i]+l[j]==s :
                    check+=1
        
        print(check)
        t-=1
arr()