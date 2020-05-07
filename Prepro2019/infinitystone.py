"""00xx: Infinity Stone"""
def main():
    """Main Func."""
    num = int(input())
    if num == 6:
        print("Snap!")
    elif 0 <= num < 6:
        print("Nope")
    else:
        print("ERROR")
main()
