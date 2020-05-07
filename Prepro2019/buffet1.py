"""0046: Buffet #1"""
def main():
    """Main Func."""
    name = input()
    num = int(input())
    print("%s can eat:" %name)
    for i in range(num):
        food = input()
        print("%d. %s" %(i+1, food))
main()
