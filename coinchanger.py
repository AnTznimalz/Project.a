"""CoinChangev1 by ศิษย์เทพปอง#2"""
def coin():
    """Func. coin for changing money"""
    change = 0
    money = int(input())
    for i in [25, 10, 5, 1]:
        change += money//i
        money = money%i
    print(change)
coin()
