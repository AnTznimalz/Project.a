"""0019 : VARIABLE"""
def main(name=input(), goods=input(), quantity=int(input()), price=float(input())):
    """Func. main"""
    print("%s : %d %s = %.0f Baht" %(name, quantity, goods, price*quantity))
main()
