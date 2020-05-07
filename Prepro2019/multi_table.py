""" Multiplication Table """
def main():
    """ Main Func. """
    print("-------------")
    for i in range(2, 13):
        for j in range(1, 13):
            print("%2d x %-2d = %d"%(i, j, i*j))
        print("-------------")
main()
