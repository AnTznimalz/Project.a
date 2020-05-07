"""(if) Red Laser Beam!!!"""
def main():
    """Main Func."""
    check = 0
    check = scan(input(), check)
    check = scan(input(), check)
    check = scan(input(), check)
    check = scan(input(), check)
    check = scan(input(), check)
    if check == 0:
        print("Red Laser Beam!!!")
def scan(name, check):
    """Scan Func."""
    if "A" in name:
        check += 1
        print(name)
    return check
main()
