"""0019 : VARIABLE"""
def main(name=input(), goods=input(), quantity=int(input()), price=float(input())):
    """Func. main"""
    print("%s : %d %s = %d Baht" %(name, quantity, goods, int(price*quantity)))
main()
