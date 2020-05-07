"""Speed limit"""
def main():
    """Main Func."""
    init = float(input()) * 3600 / 1000
    goal = int(input())
    if init < 0:
        print("Velocity can't be Negative Naja.")
    elif init == 0:
        print("This car is not moving .")
    elif init > goal:
        print("You Drive too fast.")
        print("You have exceeded the speed limit for %.2f km/hr." %(init - goal))
        print("P'Man and P'Non paid 500 Baht fine.")
    else:
        print("P'Man and P'Non is Safe with %.2f km/hr." %init)
main()
