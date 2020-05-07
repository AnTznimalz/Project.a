"""All in one I"""
def main():
    """Main Func."""
    ans = 0
    this = int(input())
    for i in range(this):
        wow = float(input())
        if i == 0:
            num = wow
            mun = wow
        hig = max(num, wow)
        num = hig
        low = min(mun, wow)
        mun = low
        ans += wow
    avg = ans / this
    print("MAX: %.2f" %hig)
    print("MIN: %.2f" %low)
    print("SUM: %.2f" %ans)
    print("AVG: %.2f" %avg)
main()
