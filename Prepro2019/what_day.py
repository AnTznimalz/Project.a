""" What day is it ??? """
def main():
    """ Main Func. """
    #0 1 2 3 4 5 6
    #9 18 27 36 45 54 63
    days = "Friday   Saturday Sunday   Monday   Tuesday  WednesdayThursday "
    num = int(input())%7 + 1
    print(days[(num-1)*9:num*9])
main()
