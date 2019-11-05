"""Extra ClockHands Thank you Lnw Mai for guiding me again to solve this problem"""
def clock(hour, minute):
    """Function clock to find out how far between hour pin and min pin"""
    change = (hour*5)+(minute/12) #hour pin >>> min pin

    #Check how far between hour pin and min pin
    if 0 <= change - minute <= 1:
        print("True")
    else:
        print("False")
clock(int(input()), int(input()))
