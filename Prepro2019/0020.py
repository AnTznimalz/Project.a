"""0020 : TAX"""
def main():
    """Func. main"""
    price = int(input())*1.1*1.07
    if price >= 0:
        print("%d" %int(price))
main()
