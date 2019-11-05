'''Gram_V1'''
def gram():
    '''Func. gram for making two gram'''
    text = input()
    emp = ''
    box = []
    wow = 0
    for i in range(len(text)-1):
        two_gram = text[i]+text[i+1]
        box.append(two_gram)
    for i in box:
        if box.count(i) > wow:
            emp = i
            wow = box.count(i)
    print(emp)
    print(wow)
gram()
