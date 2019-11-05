"""Seeker by ศิษย์เทพปอง#2"""
def find():
    """Func. find for finding sum of the Seeker number in text"""
    text = input()
    box = []
    num = ""
    total = 0
    for i in text:
        if i.isnumeric():
            num += i
        else:
            box.append(num)
            num = ""
    box.append(num)
    for i in box:
        if i.isnumeric():
            total += int(i)
    print(total)
find()
