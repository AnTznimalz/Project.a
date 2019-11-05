"""FOR!F-Ball"""
def ball(text):
    """Func. ball for finding the postion of the ball"""
    pos = "1"   #first pos is 1 at the left side
    for i in text:
        if i == "A": #swap pos1 & pos2
            if pos == "1":
                pos = "2"
            elif pos == "2":
                pos = "1"
        elif i == "B":  #swap pos2 & pos3
            if pos == "2":
                pos = "3"
            elif pos == "3":
                pos = "2"
        elif i == "C":
            if pos == "3":  #swap pos1 & pos3
                pos = "1"
            elif pos == "1":
                pos = "3"
    print(pos)
ball(input())
