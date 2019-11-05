"""Milk"""
def milk(price, cap, exc, money):
    """Func. milk for finding how many milk you can get"""
    bottle = 0
    if money != 0:
        bottle += money//price #amount of milk you would get
        bot_ex = bottle #bot_ex for calculating
        while bot_ex >= cap and cap != 0:
            bot_ex -= cap
            bot_ex += exc
            bottle += exc
    print(bottle)
milk(int(input()), int(input()), int(input()), int(input()))
