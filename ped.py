'''PedPonFire'''
def ped():
    '''Func. ped for finding ped that gas want'''
    duck = int(input())
    box = [int(input()) for i in range(duck)]
    setbx = sorted(set(box))
    gas = int(input())
    nub = 0
    for i in setbx:
        if i > gas //2:
            break
        nub += box.count(i) * box.count(gas-i)
    print(nub)
ped()
