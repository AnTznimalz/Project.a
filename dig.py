"""Rule of three"""
def find(size):
    """Func. find for finding the best price"""
    #0 at first to compare another input
    choose_this_cal = 0
    choose_this_weight = 0
    choose_this_price = 0

    #Calculate
    for _ in range(size):
        price = float(input())
        weight = float(input())
        cal = weight/price
        if cal >= choose_this_cal: #this condition is to find the best price
            choose_this_price = price
            choose_this_weight = weight
            choose_this_cal = cal
    print("%.2f %.2f"%(choose_this_price, choose_this_weight))
find(int(input()))

