'''CaesarV2'''
def caesar(num_shift, text):
    '''Func. caesar for decoding unknown password'''
    #% 26 when num_shift > 26 or < -26
    #Ex. num_shift = 27
    #input = 'a' + (27 % 26 = 1) >>> 'b'
    #Ex. num_shift = -27
    #input = 'a' + (-27 % 26 = 25) >>> 'z'
    password = ''
    alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in text:
        if i.isalpha():
            if i.islower():
                password += alp[(alp.find(i) + num_shift) % 26]
            if i.isupper():
                password += alp[((alp.find(i) + num_shift) % 26) + 26]
        else:
            password += i
    return password

def check(word):
    '''Func. check for checking word'''
    for i in 'the':
        if i in word.lower():
            return True
    return False

def possible(word):
    """Func. possible for finding how possible can word be"""
    for i in range(26):
        if check(caesar(i, word)):
            return caesar(i, word)

print(possible(input()))
