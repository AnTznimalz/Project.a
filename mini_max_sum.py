""" Mini-Max Sum """
def ans():
    """ Func. ans for finding min and max of the given arrays """
    box = [int(i) for i in input().split()]
    print(sum(box)-max(box), sum(box)-min(box))
ans()
