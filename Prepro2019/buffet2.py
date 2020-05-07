"""0047: Buffet #2"""
def main():
    """Main Func."""
    name = input()
    hate = input()
    start = 1
    food = input()
    print("%s can eat:" %name)
    if food == hate:
        print("%s hate %s!!" %(name, hate))
        return
    print("%d. %s" %(start, food))
    start += 1
    while food != hate:
        food = input()
        if food == hate:
            print("%s hate %s!!" %(name, hate))
            break
        print("%d. %s" %(start, food))
        start += 1
main()
