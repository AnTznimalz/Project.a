"""I hate Donut eventhough I like to eat it so Pizza is better,you know?
I have decoded this code for many times I'm really appreciate to thank you
my friends;Nunja & Jakkawan & whoever for helping me to solve this problem.
Friend is always friend."""
def donut(price, piece, free, need):
    """Function Donut for calculate donut"""
    get, pay, time = 0, 0, 0
    pro = piece+free
    if piece == need:
        pay += price*need
        get += pro
    elif piece > need:
        pay += price*need
        get += need
    else:
        time += int(need/pro)  #time for using pro
        without_pro = need - (time * pro) #didn't use pro
        if without_pro < piece:
            pay += (time*piece*price) + (without_pro * price)
            get += (time*pro) + without_pro
        else:
            time += 1
            pay += time*piece*price
            get += time*pro
    print(pay, get)
donut(int(input()), int(input()), int(input()), int(input()))
