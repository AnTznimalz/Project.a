'''[Final Recommend]Milk'''
def milk(cost=int(input()), cap=int(input()), exc=int(input()), money=int(input())):
    '''Func. milk for finding all the bottle of milk you will get'''
    bottle = money//cost
    free = bottle
    while free >= cap and cap != 0:
        free -= cap
        free += exc
        bottle += exc
    return bottle
print(milk())
