'''Kabata'''
def kaba(text):
    '''Func. kaba for saying that input is Kabata language or not'''
    #Kabata language don't have word 'baka'
    #But it has 'bakka'
    #Force if 'baka' in text say 'no'
    if 'baka' in text:
        return 'no'

    #replace word to get ''
    text = text.replace('bakka', '')
    text = text.replace('ta', '')
    text = text.replace('ba', '')
    text = text.replace('ka', '')

    # if len(text) != 0 >>> 'no'
    # if len(text) == 0 >>> 'yes'
    if len(text) != 0:
        return 'no'
    else:
        return 'yes'

def display():
    '''Func. display for printing yes or no'''
    for _ in range(int(input())):
        print(kaba(input()))
display()
