"""GCD_N by ศิษย์เทพปอง#2"""
def god():
    """Func. god for determine how many input"""
    num = int(input())
    cat = 0
    for i in range(num):
        if num == 1:
            cat = int(input())
        elif i == 0:
            mem = int(input())
            dog = gcd(mem, 0)
        else:
            ber = int(input())
            cat = gcd(ber, dog)
            if dog == 0 or dog != 0:
                dog = cat
    print(cat)
def gcd(wow, yay):
    """Func. gcd for finding gcd"""
    #Using recursion
    if yay == 0:
        return wow
    else:
        return gcd(yay, wow % yay)
god()
