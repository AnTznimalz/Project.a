"""Good New or Bad New ?!?"""
def main():
    """Main Func."""
    num = input()
    length = len(num)
    if len(str(int(num))) == len(num) and \
        ("111" not in num) and ("000" not in num) \
        and int(num) % 100 == 1 and int(num) // 10**(length-2) == 10:
        print(":)")
    else:
        print(":(")
main()
