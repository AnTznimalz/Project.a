"""Sushi Stair"""
def main():
    """Main Func."""
    text = input()
    space = 0
    while text != "Stop":
        print(" "*space + text)
        space += len(text)
        text = input()
main()
