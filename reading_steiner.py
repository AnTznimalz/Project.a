""" Reading Steiner """
def main():
    """ Main Func. """
    address = float(input())
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)
    address += add(address)

def add(num):
    """ Add Func. """
    total = float(input())
    print("%.6f" %(total + num))
    return total
main()
