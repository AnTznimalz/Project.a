"""All in one I"""
def main():
    """Main Func."""
    ans = 0
    for i in range(10):
        wow = float(input())
        if i == 0:
            num = wow
            mun = wow
        hig = max(num, wow)
        num = hig
        low = min(mun, wow)
        mun = low
        ans += wow
    avg = ans / 10
    print("MAX: %.2f" %hig)
    print("MIN: %.2f" %low)
    print("SUM: %.2f" %ans)
    print("AVG: %.2f" %avg)
main()
