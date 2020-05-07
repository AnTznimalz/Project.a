"""00xx: CAPSLOCK"""
def main():
    """Main Func."""
    char = input()
    if len(char) != 1:
        print("ERROR")
        return
    if 65 <= ord(char) <= 90:
        print(chr(ord(char) + 32))
    elif 97 <= ord(char) <= 122:
        print(chr(ord(char) - 32))
    else:
        print("ERROR")
main()
