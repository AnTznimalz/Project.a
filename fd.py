"""Four_Directions"""
def direct(text):
    """Func. direct for drawing direction up/down/left/right"""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
#line1
    line1 += "  *   "*(len(text))
#line2
    for i in text:
        if i == "U":
            line2 += " ***  "
        elif i == "D":
            line2 += "  *   "
        elif i == "L":
            line2 += " *    "
        elif i == "R":
            line2 += "   *  "
#line3
    for i in text:
        line3 += "* * * " if i == "U" or i == "D" else "***** "
#line4
    for i in text:
        if i == "U":
            line4 += "  *   "
        elif i == "D":
            line4 += " ***  "
        elif i == "L":
            line4 += " *    "
        elif i == "R":
            line4 += "   *  "
#line5
    line5 += "  *   "*(len(text))
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
direct(input())

