"""Binary"""
def transform(num):
    """Func. transform for transforming number base10 >>> base2"""
    box = [] #for keeping reamainder
    if num == 0:
        print(num)
    else:
        while num != 0:
            box.append(num%2)
            num = num//2
        for i in range(len(box)-1, -1, -1):
            print(box[i], end="")

transform(int(input()))
