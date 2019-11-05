"""LineSorting"""
def order(num=int(input())):
    """Func. order for sorting text"""
    box = []
    for _ in range(num):
        text = input()
        box.append(text)
    for i in sorted(box, key=len):
        print(i)
order()
