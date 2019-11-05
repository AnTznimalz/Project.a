""" Plus Minus """
def ratio():
    """ Func. ratio for calculate ratio of the given array """
    num = int(input())
    msg = input().split()
    pos = 0
    zero = 0
    neg = 0
    for i in msg:
        if int(i) > 0:
            pos += 1
        elif int(i) == 0:
            zero += 1
        else:
            neg += 1
    print("%.6f" %(pos/num))
    print("%.6f" %(neg/num))
    print("%.6f" %(zero/num))
ratio()
