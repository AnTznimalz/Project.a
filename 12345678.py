'''Break_Password'''
def psw():
    '''Func. psw for encoding password'''
    import hashlib
    for i in range(128):
        text = hashlib.sha512(input().encode()).hexdigest().upper()
    print(text)
psw()
