""" Student Searching """
def main():
    """ Main Func. """
    student = input()
    digit = int(input())
    order = int(input())
    print("Search : %d" %order)
    print("Result : %s" %student[((order-1)*digit):digit*order])
main()
