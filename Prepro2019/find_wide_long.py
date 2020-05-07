"""(loop) Find Wide x Long !!!!"""
def main():
    """Main Func."""
    text = input()
    col = 0
    for i in text:
        if i == "*":
            col += 1
    row = 0
    while text != "end":
        text = input()
        row += 1
    if row < col:
        print("%d x %d" %(row, col))
    else:
        print("%d x %d" %(col, row))
main()
