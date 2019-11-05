'''Parallelogram'''
def para():
    '''Func. para for drawing parallelogram'''
    text = input()
    num = len(text)
    for i in range(1, num+1):
        print((' '*(num-i))+text[:i])
    for i in range(1, num):
        print(text[i:]+(' '*i))
para()
