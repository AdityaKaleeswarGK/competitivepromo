def stair():
    t = int(input())
    while t > 0:
        n = int(input())
        line = input()
        inte = line.split()
        integ = [int(num) for num in inte]
        sortedint = sorted(integ)
        check = 0

        for i in range(2):
            for j in range(len(integ)):
                if integ[j] == sortedint[0]:
                    sortedint.pop(0)
                if len(sortedint)==0 :
                    check=1
                    break
            if (check==1) :
                break
        if check ==1 :
            print("Yes")
        else :
            print("No")

        t -= 1

stair()