""" Balloon Game """
def main():
    """ Main Func. """
    jack = cal(int(input()))
    rew = cal(int(input()))
    pok = cal(int(input()))
    fight = cal(int(input()))
    jub = cal(int(input()))
    print("P'Jack won " + jack)
    print("P'Rew won " + rew)
    print("P'Pok won " + pok)
    print("P'Fight won " + fight)
    print("P'Jub won " + jub)
def cal(score):
    """ Cal Func. """
    txt = ""
    if score == 0:
        txt += 'nothing.'
    if 1 <= score <= 3:
        txt += 'a pen.'
    if 4 <= score <= 5:
        txt += 'a notebook.'
    if 6 <= score <= 7:
        txt += 'a key chain.'
    if 8 <= score <= 9:
        txt += 'a teddy bear.'
    if score == 10:
        txt += 'a large teddy bear.'
    return txt
main()
