"""00XX: Water Tank"""
import math
def main():
    """Main Func."""
    goal = float(input())
    diameter = float(input())/2
    hig = float(input())
    vol = math.pi* (diameter**2) * hig
    this = vol
    level = 1
    if goal == 0:
        print("Volume : 0.00 >= 0.00 Water")
        print(" - Enough")
        print("Level : 0")
        return
    while vol < goal:
        print("Volume : %.4f < %.2f Water" %(vol, goal))
        print(" - Increase the height")
        print()
        level += 1
        vol += this
    print("Volume : %.2f >= %.2f Water" %(vol, goal))
    print(" - Enough")
    print("Level : %d" %level)
main()
