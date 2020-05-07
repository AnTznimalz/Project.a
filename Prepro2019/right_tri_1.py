"""Right Triangle #1"""
import math
def main():
    """Main Func."""
    corner = math.radians(float(input()))
    skip = float(input())
    ans = skip / math.sin(corner)
    print("c = %.2f" %ans)
main()
