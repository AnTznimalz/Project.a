"""CoPrime V1"""
def cop(num1, num2):
    """Func. cop for finding coprime"""
    mnum = 0
    if num1 == 0 and num2 == 0:
        mnum = 0
    elif num1 == 0 and num2 != 0:
        mnum = num2
    elif num1 != 0 and num2 == 0:
        mnum = num1
    elif num1 > num2:
        for i in range(1, (num2)+1):
            if num1%i == 0 and num2%i == 0:
                if mnum <= i:
                    mnum = i
    elif num1 == num2:
        mnum = num1
    elif num1 < num2:
        for i in range(1, (num1)+1):
            if num1%i == 0 and num2%i == 0:
                if mnum <= i:
                    mnum = i
    print("YES \n"+"1" if mnum == 1 else "NO \n"+str(mnum))
cop(int(input()), int(input()))
