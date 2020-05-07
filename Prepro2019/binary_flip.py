"""00xx: Binary Flip"""
def main():
    """Main Func."""
    num = input()
    for i in num:
        if i == "0":
            print(1, end="")
        else:
            print(0, end="")
main()
