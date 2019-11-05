"""Missing Numbers"""
def order(num, box, newbox):
    """Func. order for ordering the missing number"""
    for _ in range(num):
        num2 = int(input())
        box.append(num2)
        if num2 == 0:
            break
    box.sort()
    for i in range(num+1):
        newbox.append(i)
    for i in newbox:
        if i not in box:
            print(i)
order(int(input()), [], [])
