"""Restaurant"""
def manage(cost, pro, dis, more):
    """Func. manage for saying how the price is"""
    dis_price = (cost+more)*(1- dis/100)
    if cost < pro:
        if cost > dis_price:
            print("Yes %.3f"%abs(cost-dis_price))
        elif cost < dis_price:
            print("No %.3f"%abs(cost-dis_price))
        else:
            print("Yes")
    elif cost == pro:
        if more > 0:
            result = abs((cost*(1-dis/100)) - dis_price)
            if result > 0:
                print("No %.3f"%result)
            else:
                print("Yes")
        elif more == 0:
            print("Yes")
manage(float(input()), float(input()), float(input()), float(input()))
