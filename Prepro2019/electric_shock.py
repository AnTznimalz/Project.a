"""Electric Shock"""
def main():
    """Main Func."""
    txt = ' ' + input() + ' '
    nub = 0
    stack = 0
    for i in txt:
        if i == ' ':
            if stack == 0:
                stack += 1
            elif stack == 2:
                nub += 1
                stack -= 1
        elif (i == "e" or i == "E") and stack == 1:
            stack = 2
        else:
            stack = 0
    print(nub)
main()
