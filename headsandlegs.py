'''Heads and Legs'''
def nub(head=int(input()), leg=int(input())):
    '''Func. nub for counting how may animals and how possible'''
    rabbits = (leg-(2*head))//2
    birds = head - rabbits
    if (4*rabbits) + (2*birds) == leg and rabbits >= 0 and birds >= 0:
        print(rabbits, birds)
    else:
        print('Impossible')
nub()
