'''[Final Recommend]Safe'''
def safe(password=input(), lock=input()):
    '''Func. safe for turn password'''
    nub = 0
    for i in range(len(lock)):
        text_p = ord(password[i]) 
        text_l = ord(lock[i])
        distance = abs(text_p - text_l)
        if distance <= 13:
            nub += distance
        else:
            nub += 26-distance
    print(nub)
safe()
