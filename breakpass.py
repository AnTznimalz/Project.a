'''Break_Password by ศิษย์เทพปอง#2'''
import hashlib
def psw(password):
    '''Func. psw for encoding password'''
    for i in range(555555):
        f_digit = '%05d'%i
        if password == hashlib.sha512(f_digit.encode('utf-8')).hexdigest().upper():
            return f_digit
print(psw(input()))
