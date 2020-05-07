""" Swapping """
def main():
    """ Main Func. """
    txt = input()
    w_1 = input()
    w_2 = input()
    txt = txt.replace(w_1, "***").replace(w_2, w_1).replace("***", w_2)
    print(txt)
main()
