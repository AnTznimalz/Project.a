""" Apple && Orange """
def dis():
    """ Func. dis for calculate distance """
    a, o = 0,0
    i, f = input().split()
    a_, o_ = input().split()
    na, no = input().split()
    app = input().split()
    ora = input().split()
    for j in app:
        if int(i) <= int(j) + int(a_) <= int(f):
            a += 1
    for j in ora:
        if int(i) <= int(j) + int(o_) <= int(f):
            o += 1
    print(a)
    print(o)
dis()
