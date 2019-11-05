'''Point Sorting'''
def order():
    '''Func. order for ordering point'''
    data = int(input())
    box = []
    for _ in range(data):
        info = int(input())
        for _ in range(info):
            small_dat = input()
            box.append(small_dat.split())
        for p_x, p_y in box:
            p_x, p_y = int(p_x), int(p_y)
        box.sort(key=lambda x: x[0], reverse=True)
        box.sort(key=lambda x: x[0] + x[1], reverse=True)
        for p_x, p_y in box:
            print(p_x, p_y)
        box = []
order()
