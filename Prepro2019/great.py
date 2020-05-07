"""Great"""
def main():
    """Main Func."""
    g_1, g_2, g_3 = 0, 0, 0
    for _ in range(int(input())):
        food = input()
        if food == "salmon" or food == "bingsu" or food == "mint":
            g_1 += 1
        elif food == "whey" or food == "tempura" or food == "steak":
            g_2 += 1
        elif food == "yakiniku" or food == "bbq" or food == "meat":
            g_3 += 1
    high = max(g_1, g_2, g_3)
    if g_1 == 0 and g_2 == 0 and g_3 == 0:
        print("This is fatty G .")
        return
    if g_1 == g_2 == high or g_2 == g_3 == high or g_1 == g_3 == high:
        print("100% P'Great")
        return
    if high == g_1:
        print("The Greatest Great")
    if high == g_2:
        print("The Athlete Great")
    if high == g_3:
        print("The Eater Great")
main()
