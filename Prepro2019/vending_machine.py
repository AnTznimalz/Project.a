"""1017: Vending machine"""
def main():
    """Func. Main"""
    pay = int(input())
    price = int(input())
    change = pay - price
    hundred = change // 100
    change -= hundred * 100
    fifty = change // 50
    change -= fifty * 50
    twenty = change // 20
    change -= twenty * 20
    ten = change // 10
    change -= ten * 10
    five = change // 5
    change -= five * 5
    two = change // 2
    change -= two * 2
    one = change // 1
    change -= one * 1
    print("%d, %d, %d, %d, %d, %d, %d" %(hundred, fifty, twenty, ten, five, two, one))
main()
    