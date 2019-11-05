'''Progressive_Tax'''
def tax():
    '''Func. tax for calculating tax for people who have salary'''
    money = int(input())
    pro = 0
    if money > 4000000:
        money = money-4000000
        pro += 0.35*money
        money = 4000000
    if 2000000 < money <= 4000000:
        money = money-2000000
        pro += 0.30*money
        money = 2000000
    if 1000000 < money <= 2000000:
        money = money-1000000
        pro += 0.25*money
        money = 1000000
    if 750000 < money <= 1000000:
        money = money-750000
        pro += 0.20*money
        money = 750000
    if 500000 < money <= 750000:
        money = money-500000
        pro += 0.15*money
        money = 500000
    if 300000 < money <= 500000:
        money = money-300000
        pro += 0.10*money
        money = 300000
    if 150000 < money <= 300000:
        money = money-150000
        pro += 0.05*money
        money = 150000
    print(int(pro))
tax()
    