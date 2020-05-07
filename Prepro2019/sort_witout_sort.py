""" Sort without Sort """
def main():
    """ Main Func. """
    box = [int(input()) for i in range(int(input()))]
    print(box)
    a = box.sort(reverse=True)
    print(a)
main()