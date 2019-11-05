"""Refrigerator"""
def refrigerator():
    """Func. refrigerator for finding the longest day for healing food"""
    box = []
    day = 0
    _ = int(input())
    exp_day = input().split()
    for i in exp_day:
        box.append(int(i))
    box.sort()
    while box[0] != 0:
        for i in range(1, len(box)):
            box[i] = box[i] - 1
        day = day + 1
        box.sort()
    print(day)
refrigerator()
