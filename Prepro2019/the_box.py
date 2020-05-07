"""0045: The BOX"""
def main():
    """Main Func."""
    num = int(input())
    for _ in range(num):
        for _ in range(num):
            print("* ", end="")
        print("")
main()
