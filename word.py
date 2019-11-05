'''WordSequence II'''
def order():
    '''Func. order for printing word'''
    text_1 = list(input())
    text_2 = list(input())
    while len(text_1) != len(text_2):
        if len(text_1) > len(text_2):
            text_2.append('')
        else:
            text_1.append('')
    print(*text_1, sep='')
    for i in range(len(text_1)):
        if text_1[i] != text_2[i]:
            text_1[i] = text_2[i]
        print(*text_1, sep='')
order()
