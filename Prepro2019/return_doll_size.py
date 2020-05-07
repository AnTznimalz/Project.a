"""00XX: Return of Doll's Size"""
def main():
    """Main Func."""
    small = int(input())
    medium = int(input())
    large = int(input())
    if (small > medium and small < large) or (small > large and small < medium):
        print(small, "cm.")
    elif (large > medium and large < small) or (large > small and large < medium):
        print(large, "cm.")
    else:
        print(medium, "cm.")
main()
