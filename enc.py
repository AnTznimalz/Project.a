"""Run Length Encoding"""
def nub(word, count):
    """Func. nub for counting alphabet"""
    for _ in range(len(word)):
        if len(word) >= 2:
            check = word[:2] #check two letters that beside
            if check[0] == check[1]:
                count += 1
                word = word[1:] #cut the first letter
            else:
                print(str(count)+word[0], end="")
                word = word[1:]
                count = 1
    print(str(count)+word[0], end="")
nub(input(), 1)
