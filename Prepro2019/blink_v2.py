"""00XX: Blink"""
from math import gcd
def main():
    """Main Func."""
    freq_1 = int(input())
    freq_2 = int(input())
    time = int(input())
    if time % gcd(freq_1, freq_2) == 0:
        print("yes")
    else:
        print("no")
main()
