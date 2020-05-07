""" itkmitl """
def main():
    """ Main Func. """
    msg = input().lower()
    if msg.count("k") >= 1 and msg.count("m") >= 1 and msg.count("i") >= 2\
        and msg.count("t") >= 2 and msg.count("l") >= 1:
        print("Yes")
    else:
        print("No")
main()
