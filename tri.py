"""Plan B"""
def main():
    """Main Func."""
    side1 = float(input())
    side2 = float(input())
    side3 = float(input())
    big1 = side1**2
    big2 = side2**2
    big3 = side3**2
    if side1 > side2 and side1 > side3:
        if big1+0.01 >= big2+big3 or big1+0.01 <= big2+big3 \
        or big1 >= big2+big3+0.01 or big1 <= big2+big3+0.01:
            print("Yes")
        else:
            print("No")
    elif side2 > side1 and side2 > side3:
        if big2+0.01 >= big1+big3 or big2+0.01 <= big1+big3 \
        or big2 >= big1+big3+0.01 or big2 <= big1+big3+0.01:
            print("Yes")
        else:
            print("No")
    elif side3 > side1 and side3 > side2:
        if big3+0.01 >= big2+big1 or big3+0.01 <= big2+big1 \
        or big3 >= big2+big1+0.01 or big3 <= big2+big1+0.01:
            print("Yes")
        else:
            print("No")


main()
