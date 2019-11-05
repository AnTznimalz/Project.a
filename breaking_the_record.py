""" Breaking the record """
def score():
    """ Func. score for recording the score """
    game = int(input())
    s = [int(i) for i in (input().split())]
    h, l = 0, 0 
    for i in range(game):
        if i == 0:
            hi, lo = s[0], s[0]
        if s[i] > hi:
            h += 1
            hi = s[i]
        if s[i] < lo:
            l += 1
            lo = s[i]
    print(h, l)
score()
