"""HorizontalHistogram by ศิษย์เทพปอง#2"""
def draw():
    """Func. draw for drawing histogram graph"""
    box_a = []
    text = input()
    for i in text:
        box_a.append(i)
        box_a.sort()
    for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        nub_a = box_a.count(i)
        if nub_a != 0:
            print('%s : '%i, end='')
            for j in range(nub_a):
                if j%5 == 0 and j != 0:
                    print('|-', end='')
                else:
                    print('-', end='')
            print()
draw()
