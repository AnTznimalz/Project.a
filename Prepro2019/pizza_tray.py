"""Pizza's Tray"""
import math
def main():
    """Main Func."""
    pizza = int(input())
    tray = math.ceil(pizza/8)
    print(tray)
main()
