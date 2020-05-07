"""Print List"""
# def main():
#     """Main Func."""
#     box = input()
#     name = input()
#     if name not in box:
#         print("Not in group.")
# main()
def main():
    """ Main Func. """
    box = []
    goods = ''
    bad = []
    stack = 1
    while 1:
        goods = input()
        if goods == "My list":
            break
        if goods != "Remove" and stack == 1:
            box.append(goods)
        elif goods != "Remove" and stack == 0:
            box.remove(goods)
            bad.append(goods)
        else:
            if stack == 1:
                stack = 0
    for i in bad:
        print("%s is removed" %i)
    print()
    print("--- My list ---")
    for i in box:
        print("%d. %s" %(box.index(i)+1, i))
main()
