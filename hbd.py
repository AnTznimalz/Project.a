""" Birthday Cake Candles """
def hbd():
    """ Func. hbd for counting candle that the owner's birthday can blow out """
    num = int(input())
    lst = [int(i) for i in input().split()]
    a = max(lst)
    b = 0
    for i in range(num):
        if lst[i] == a:
            b += 1
    print(b)
hbd()
