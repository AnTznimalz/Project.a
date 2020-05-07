"""00xx: Leap Year"""
def main():
    """Main Func."""
    year = int(input())
    if year <= 0:
        print("This year doesn't exist.")
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(year, "is leap year.")
        else:
            print(year, "is not leap year.")
main()
