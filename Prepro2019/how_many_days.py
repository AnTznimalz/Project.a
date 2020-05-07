"""00xx: How Many Days"""
def main():
    """Main Func."""
    month = int(input())
    year = int(input())
    if year <= 0 or month < 1 or month > 12:
        print("Invalid month or year.")
    else:
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                print("29 Days.")
            else:
                print("28 Days.")
        elif month == 4 or month == 6 or month == 9 or month == 11:
            print("30 Days.")
        else:
            print("31 Days.")
main()
