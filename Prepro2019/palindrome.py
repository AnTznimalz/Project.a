""" Palindrome """
def main():
    """Main Func."""
    txt = input().lower()
    msg = ""
    for i in txt:
        if i.isalpha():
            msg += i
    print(msg == msg[::-1])
main()
