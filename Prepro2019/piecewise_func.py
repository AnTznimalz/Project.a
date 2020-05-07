"""Piecewise-Defined Function"""
def main():
    """Main Func."""
    num = compute(float(input()))
    print("%.2f" %num)
def compute(num):
    """Compute Func."""
    if num <= -1:
        ans = num**2 +1
    elif -1 < num < 2:
        ans = num + 4
    else:
        ans = 5
    return ans
main()
