"""Extra Taxi V.1 Proudly thank you LnW Mai for helping me to solve this problem"""
def taxi(distance, time):
    """Function For Calculating Taxi Price"""
    money = 35
    extra = time*1.50
    if 0 <= distance <= 1:
        pass
    elif 2 <= distance <= 12:
        money += (distance-1)*5
    elif 13 <= distance <= 20:
        money += 55 + (distance-12)*5.50
    elif 21 <= distance <= 40:
        money += 99 + (distance-20)*6
    elif 41 <= distance <= 60:
        money += 219 + (distance-40)*6.50
    elif 61 <= distance <= 80:
        money += 349 + (distance-60)*7.50
    elif 81 <= distance:
        money += 499 + (distance-80)*8.50
    if money%1 != 0:
        money = int(money)+1
    if int(money)%2 == 0:
        money = int(money) + 1
    else:
        money = int(money)
    if int(extra)%2 != 0:
        extra = int(extra) - 1
    elif int(extra)%2 == 0:
        extra = int(extra)
    total = money + extra
    print(total)
taxi(int(input()), int(input()))

