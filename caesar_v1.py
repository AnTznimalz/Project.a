'''CaesarV1 learn from Mr.Saran Hanthongkam(P'Winner)'''
def caesar():
    '''Func. caesar for decoding unknown password'''
    num_shift = int(input()) % 26
    #% 26 when num_shift > 26 or < -26
    #Ex. num_shift = 27
    #input = 'a' + (27 % 26 = 1) >>> 'b'
    #Ex. num_shift = -27
    #input = 'a' + (-27 % 26 = 25) >>> 'z'
    text = input()
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
    print(password)
caesar()
