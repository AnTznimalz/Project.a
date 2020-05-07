"""The function within"""
import math as m
def main():
    """Main Func."""
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    ans = three(one(num_1+num_2), one(num_1+num_3), two(one(num_1), num_2+num_3))
    print("%.2f" %ans)
def one(num):
    """First Func."""
    ans = m.pi*num
    return ans
def two(num_1, num_2):
    """Second Func."""
    ans = m.sqrt(num_1 + num_2)
    return ans
def three(num_1, num_2, num_3):
    """Third Func."""
    ans = ((num_1 + num_3)**2) - (num_1*num_2) + num_2 + num_3
    return ans
main()
