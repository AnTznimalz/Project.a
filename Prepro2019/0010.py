"""0010: More_String"""
def main(message=input(), num=int(input())):
    """Func. main"""
    for i in range(0, num):
        if i == num-1:
            print(message)
        else:
            print(message+"_", end="")
main()