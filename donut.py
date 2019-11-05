"""Donut"""
def donut(price, piece, free, need):
    """Function Donut for finding price and piece of donut"""
    pay, get = 0, 0
    pro = piece + free
    if piece == need:
        get += pro
        pay += price*piece
    elif piece > need:
        get += need
        pay += price*need
    else:
        if pro >= need:
            get += pro
            pay += price*piece
        elif pro < need:
            if need%pro == 0:
                get += (need//pro)*pro
                pay += (need//pro)*(price*piece)
            elif need%pro != 0:
                if need-((need//pro)*pro) < piece:
                    get += (need//pro)*pro +(need-(need//pro)*pro)
                    pay += ((need-(pro*(need//pro)))*price) + (need//pro)*(price*piece)
                else:
                    get += pro*((need//pro))+(need//pro)*pro
                    pay += (price*piece)*((need//pro)+1)
    print("%d %d"%(pay, get))
donut(int(input()), int(input()), int(input()), int(input()))
