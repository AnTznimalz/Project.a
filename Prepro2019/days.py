""" Days """
def main():
    """ Main Func."""
    days = "MONTUEWEDTHUFRISATSUN"
    num = int(input())
    if 1 <= num <= 7:     
        print(days[(num-1)*3:num*3])
    else:
        print("Invalid Day")
main()
