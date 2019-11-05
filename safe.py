"""Safe"""
def nub():
    """Func. nub for counting how many times to decoding password"""
    password = input()
    lock = input()
    count = 0
    alp = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, \
    'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,\
     'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    for i in range(len(lock)):
        ans = alp[password[i]]-alp[lock[i]]
        if ans < -13:
            ans += 26
        elif 0 > ans >= -13:
            ans = abs(ans)
        elif ans > 13:
            ans = 26-ans
        count += ans
    print(count)
nub()
