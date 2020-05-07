""" Revers Card Open """
def reverse():
    """Reverse Func."""
    msg = input()
    txt = ""
    for i in msg:
        txt = i + txt
    print(txt)
reverse()
