"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def again(sentence):
    """Func. again for finding word that have at least two vowels"""
    dog = sentence.strip(".")
    box = dog.split(" ")
    newbox = []
    nub = 0
    for i in box:
        nub = i.count('a')
        nub += i.count('e')
        nub += i.count('i')
        nub += i.count('o')
        nub += i.count('u')
        if nub > 1:
            newbox.append(i.strip("."))
    newbox.sort()
    for i in newbox:
        print(i)
    if newbox == []:
        print("Nope")
again(input())
