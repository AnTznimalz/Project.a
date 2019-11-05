"""Binary"""
def change(num):
    """Func. change for transform numbase10>>>base2"""
    box = []
    box.append(str(0 if num%2 == 0 else 1))
    while num > 1:
        num = num // 2
        box.append(str(0 if num%2 == 0 else 1))
    box.reverse()
    print(''.join(box))
change(int(input()))
