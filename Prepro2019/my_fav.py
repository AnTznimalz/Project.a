"""My Favourite"""
def main():
    """Main Func."""
    goal = input()
    food = input()
    while food != goal:
        print("Nope")
        food = input()
    print("Correct !")
main()
