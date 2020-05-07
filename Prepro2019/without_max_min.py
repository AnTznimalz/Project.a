"""Highest, Lowest without max(), min()"""
def main():
    """Main Func."""
    num_1 = int(input())
    highest = num_1
    lowest = num_1
    num_2 = int(input())
    highest = hig(highest, num_2)
    lowest = low(lowest, num_2)
    num_3 = int(input())
    highest = hig(highest, num_3)
    lowest = low(lowest, num_3)
    num_4 = int(input())
    highest = hig(highest, num_4)
    lowest = low(lowest, num_4)
    num_5 = int(input())
    highest = hig(highest, num_5)
    lowest = low(lowest, num_5)
    print("Highest Value : %d" %highest)
    print("Lowest Value  : %d" %lowest)
def hig(high, num):
    """Finding highest value"""
    if num > high:
        return num
    return high
def low(lowy, num):
    """Finding lowest value"""
    if num < lowy:
        return num
    return lowy
main()
    