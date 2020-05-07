""" The Position """
def main():
    """ Main Func. """
    msg = input().lower()
    goal = input()
    f = msg.find(goal.lower())
    box = []
    box.append(f+1)
    f += 1
    nub = 0
    if goal.lower() in msg:
        while nub != len(msg):
            box.append(msg.find(goal.lower(), f)+1)
            f += 1
            nub += 1
        box = list(set(box))
        box.sort()
        box.remove(0)
        print("The position of %s is here: " %(goal), end="")
        print(*box)
    else:
        print("The position of %s is here:" %(goal))
main()
