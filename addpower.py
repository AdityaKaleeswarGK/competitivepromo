def add():
    t = int(input())
    
    while t > 0:
        num = input()
        integers = [int(x) for x in num.split()]
        N = integers[0]
        K = integers[1]
        diff = bin(N - K)[2:]
        rev = diff[::-1]
        c = 0
        
        for i in rev:
            if i == '1':
                c += 1
        
        print(c)
        
        t -= 1 

add()
