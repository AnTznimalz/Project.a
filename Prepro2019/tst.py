""" Test """
def main():
    """ Main Func."""
    msg = ''
    check = 1
    milk = 0
    gel = 0
    whip = 0
    sug = 0
    van = 0
    sour = 0
    while msg != 'bake':
        msg = input()
        if msg != 'bake':
            lst = (msg.split())
            if lst[0] == 'milk' and (lst[2] == 'cup' or lst[2] == 'cups'):
                milk += float(lst[1])
            elif lst[0] == 'gelatin' and lst[2] == 'tsp':
                gel += float(lst[1])
            elif lst[0] == 'whip_cream' and (lst[2] == 'cup' or lst[2] == 'cups'):
                whip += float(lst[1])
            elif lst[0] == 'sugar' and lst[2] == 'tsp':
                sug += float(lst[1])
            elif lst[0] == 'vanilla_extract' and lst[2] == 'tsp':
                van += float(lst[1])
            elif lst[0] == 'sour_cream' and (lst[2] == 'cup' or lst[2] == 'cups'):
                sour += float(lst[1])
            else:
                check = 0
        else:
            break
    if check and milk == 1 and gel == 2.5 and whip == 2 and sug == 25\
         and van == 1 and sour == 1:
        print("You nailed it!")
    else:
        print("You failed it.")
main()
