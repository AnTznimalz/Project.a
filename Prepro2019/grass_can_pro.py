""" Grass Can Promotion """
def main():
    """ Main Func. """
    price = float(input())
    pro = int(input())
    free = int(input())
    want = int(input())
    get = pro + free
    if want % get < pro:
        buy = (want // get) * pro + want % get 
    else:
        buy = (want // get) * pro + pro
    pay = buy*price
    pieces = buy + buy // pro*free
    print("%.2f Baht\n%d"%(pay, pieces))
main()
