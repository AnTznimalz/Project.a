'''Diamond '''
def dig():
    '''Func. dig for digging the highest value of diamond'''
    floor, piece = int(input()), int(input())
    box = []
    for _ in range(floor):
        diamond = input().split()
        box.append(diamond)
        for i in range(len(diamond)):
    print(box)
dig()
