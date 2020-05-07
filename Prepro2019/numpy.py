""" Number Pyramid """
def main():
    """ Main Func. """
    num = input()
    for i in range(len(num)):
        for j in range(-(len(num)-1), len(num)):
            if i >= abs(j):
                print(num[abs(j)], end="")
            else:
                print(" ", end="")
        print()
main()
