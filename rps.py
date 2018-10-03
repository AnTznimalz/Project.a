"""RockPaperScissor"""
def find(text):
    """Func. find for finding the winner of the game"""
    apple = 0 #apple is for collecting score of player A
    boy = 0 #boy is for collecting score of player B
    while True:
        if len(text) < 2:
            break
        check = text[:2] #range[:2] for checking for once 2 words
        if "RP" in check:   #B wins A
            boy += 1
        elif "SP" in check: #A wins B
            apple += 1
        elif "PR" in check:  #A wins B
            apple += 1
        elif "PS" in check: #B wins A
            boy += 1
        elif "RS" in check: #A wins B
            apple += 1
        elif "SR" in check: #B wins A
            boy += 1
        text = text[2:] #for cutting the 2 words that already used
    if apple > boy:
        print("A win %d-%d"%(apple, boy))
    elif apple < boy:
        print("B win %d-%d"%(boy, apple))
    else:
        print("DRAW %d"%boy)
find(input())
