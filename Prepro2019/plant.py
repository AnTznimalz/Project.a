"""Plant"""
def main():
    """Main Func."""
    num = int(input())
    if num < 1 or num > 30:
        print("Invalid date.")
    else:
        if num % 2 != 0 and num % 3 != 0:
            print("Nothing.")
        else:
            if num % 2 == 0 and num % 3 == 0:
                print("Both of them.")
            elif num % 2 == 0:
                print("Cactus")
            elif num % 3 == 0:
                print("Bowstring Hemp")
main()
