"""00XX: 0 to n odd only !!!"""
def main():
    """Main Func."""
    for i in range(int(input())):
        if i % 2 != 0:
            print(i, end="\n")
main()
