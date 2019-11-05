'''GCD_N by ศิษย์เทพปอง#2'''
def gcd():
    '''Func. gcd for finding gcd of N numbers'''
    last = int(input())
    cat = 1
    rat = 0
    for _ in range(last):
        num = int(input())
        dog = cal(num)
        if dog != 0:
            if dog % cat == 0 or cat % dog == 0:
                rat = cat
                cat = dog
            elif dog % cat != 0:
                rat = cat
                cat = dog % cat
            elif cat % dog != 0:
                rat = cat
                cat = cat % dog
        else:
            pass
    print(rat)
def cal(num):
    '''Func. cal for calculating'''
    return num
gcd()
