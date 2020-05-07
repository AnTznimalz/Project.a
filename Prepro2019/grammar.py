""" Grammar """
def main():
    """ Main Func. """
    sentence = input()
    txt = ""
    for i in range(len(sentence)):
        if i == 0:
            txt += sentence[i].upper()
        elif i == len(sentence) - 1:
            txt += "."
        else:
            txt += sentence[i]
    print(txt)
main()
