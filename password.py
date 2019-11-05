'''Password by ศิษย์เทพปอง#2'''
def psw():
    '''Func. psw for encoding password'''
    import hashlib
    text = hashlib.sha512(input().encode()).hexdigest().upper()
    print(text)
psw()
