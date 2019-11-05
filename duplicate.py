"""Duplicate I"""
def dup(group_a=int(input()), group_b=int(input())):
    """Func. dup for finding who are in both group_a & group_b"""
    box, boxz = [], []
    dog = 0
    for _ in range(group_a):
        member_a = int(input())
        box.append(member_a)
    for _ in range(group_b):
        member_b = int(input())
        box.append(member_b)
    box.sort()
    for i in range(len(box)):
        if box[i] == box[i-1]:
            boxz.append(box[i])
            dog = 1
    if dog == 0:
        print("Nope")
    else:
        rewind = reversed(boxz)
        for i in rewind:
            print(i)
dup()
