'''[Final Recommend]LineSorting'''
def linesort():
    '''Func. linesort for sorting line'''
    print(*sorted([input() for i in range(int(input()))], key=len), sep='\n')
linesort()
