"""VerticalHistogram by ศิษย์เทพปอง#2"""
def make(text=input()):
    """Func. make for making vertical histogram"""
    alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    box = []
    dic = dict()
    val = 0
    #collect alphabets into list
    for i in alp:
        if i in text:
            dic[i] = text.count(i)
            box.append(i)
            if text.count(i) > val:
                val = text.count(i)
            else:
                val = val
    for i in range(val, 0, -1):
        print("%03d "%i, end="")
        for wow in sorted(dic, key=str.swapcase):
            if dic[wow] >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print("   ", *box, sep=" ")
make()
