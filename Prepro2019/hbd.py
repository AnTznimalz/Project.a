"""Happy Birthday"""
def main():
    """Main Func."""
    day = int(input())
    month = int(input())
    state = (day == 17 and month == 6)
    print("Happy Birthday !!!" * state)
main()
