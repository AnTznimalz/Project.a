""" Check This """
def main():
    """ Main Func. """
    txt = input()
    for i in txt:
        if i.isdigit():
            print(i, type(int(i)))
        else:
            print(i, type(i))
main()
 