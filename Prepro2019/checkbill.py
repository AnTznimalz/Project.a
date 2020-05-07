"""Check bill please!"""
def main():
    """Main Func."""
    money = float(input())
    vat = money * 0.07
    ser = (money + vat) * 0.1
    pay = money + vat + ser
    print("%.2f" %pay)
main()