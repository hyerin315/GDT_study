def gugu():
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    if ((2 <= a) and (a <= 9)) and ((2 <= b) and (b <= 9)):
        for j in range(1, 10):
            if a > b:
                for i in range(a, b-1, -1):
                    ij = i * j
                    if ij < 10:
                        print(i, "*", j, "= ", ij, end="   ")
                    else:
                        print(i, "*", j, "=", ij, end="   ")
                print("")
            else:
                for i in range(a, b + 1):
                    ij = i * j
                    if ij < 10:
                        print(i, "*", j, "= ", ij, end="  ")
                    else:
                        print(i, "*", j, "=", ij, end="  ")
                print("")

    else:
        print("INPUT ERROR!")
        gugu()


gugu()


