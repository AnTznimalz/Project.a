"""Run Length Decoding"""
def change(word):
    """Func. change for changing number to alphabet"""
    text = ""   #for keeping alphabets
    num = "" #for keeping numbers
    for i in word:
        if i.isnumeric():
            num += i
        elif i.isalpha():
            text += i
            print(int(num)*text, end="")
            text = ""
            num = ""
change(input())
