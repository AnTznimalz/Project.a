"""Guess Game"""
def main():
    """Main Func."""
    goal = int(input())
    num = int(input())
    while num != goal:
        if num < goal:
            print("Too low.")
        else:
            print("Too high.")
        num = int(input())
    print("Correct ! It's %d." %goal)
main()
