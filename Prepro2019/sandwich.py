"""Sandwich"""
def sand():
    """Func. sand"""
    num = com(com(com(float(input()))))
    print("%.2f" %num)
def com(wow):
    """Func. com"""
    return (wow%5 + wow//4)**2
sand()
