def permute():
    t = int(input())
    while t > 0:
        s1 = input()
        s2 = input()

        fs1 = [0, 0, 0, 0] 
        fs2 = [0, 0, 0, 0] 

        if len(s1) % len(s2) == 0 and len(s2) <= len(s1):
            for letter in s1:
                if letter == 'C':
                    fs1[0] += 1
                elif letter == 'O':
                    fs1[1] += 1
                elif letter == 'K':
                    fs1[2] += 1
                elif letter == 'F':
                    fs1[3] += 1

            for letter in s2:
                if letter == 'C':
                    fs2[0] += 1
                elif letter == 'O':
                    fs2[1] += 1
                elif letter == 'K':
                    fs2[2] += 1
                elif letter == 'F':
                    fs2[3] += 1

            permute_possible = all(fs2[i] <= fs1[i] for i in range(4))
            efs1 = int(len(s1) / len(s2))

            if permute_possible and all(i == efs1 for i in fs1):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
        t -= 1 
permute()