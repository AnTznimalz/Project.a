"""Ascending"""
def asc(box):
    """Func. asc for ordering from the smallest number >>> the largest number """
    for _ in range(5):
        num = int(input())
        box.append(num)
    box.sort()
    for i in box:
        print(i)
asc([])
