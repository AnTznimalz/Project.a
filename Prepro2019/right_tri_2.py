"""Right Triangle #2"""
import math
def main():
    """Main Func."""
    corner = math.radians(float(input()))
    skip = float(input())
    ans = 0.5 * skip * (skip / math.tan(corner))
    print("Area = %.3f" %ans)
main()
