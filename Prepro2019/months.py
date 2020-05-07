""" Months """
def main():
    """ Main Func."""
    months = "January  February March    April    May      June     July     August   SeptemberOctober  November December "
    num = int(input())     
    print(months[(num-1)*9:num*9])
main()
