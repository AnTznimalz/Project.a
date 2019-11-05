"""Classify by ศิษย์เทพปอง#2"""
def separate():
    """Func. separate for classifying"""
    box = []
    dic_a = {}
    while True:
        num = input()
        if num == 'END':
            break
        box.append(num)
    box = sorted(box)
    for i in box:
        dic_a[i[0:2]] = {}
    for i in box:
        dic_a[i[0:2]][i[2:4]] = 0
    for key in dic_a:
        for i in box:
            if key == i[0:2]:
                dic_a[i[0:2]][i[2:4]] += 1
    box = sorted(dic_a)
    for i in box:
        change = 0  #change is a value for calculated.
        for j in sorted(dic_a[i]):
            if change == 0:
                print(i, int(j), dic_a[i][j])
                change = 1
            else:
                print("-- %d %s"%(int(j), dic_a[i][j]))
separate()
