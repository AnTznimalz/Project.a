"""Shrek"""
def main():
    """Main Func."""
    text = input()
    nub = 0
    while text != "Sleep":
        if text == "Shrek":
            nub += 1
        text = input()
    print("Shrek Count: %d" %nub)
main()
