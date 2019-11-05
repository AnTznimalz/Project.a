"""Run Length Decoding"""
def change(word):
    """Func. change for changing number to alphabet"""
    for _ in range(len(word)):
        if word.isalnum():
            check = word[:2]
            num = int(check[0])
            print(num)
            alp = check[1]
            print(alp)
            word = word[2:] #cut num and alphabet
        print(num*alp, end="")
change(input())
