box = set()
def cal(num,wow):
    if wow+6 <= num:
        box.add(wow+6)
        cal(num, wow+6)
    if wow+9<=num:
        box.add(wow+9)
        cal(num, wow+9)
    if wow+20<=num:
        box.add(wow+20)
        cal(num, wow+20)
num = int(input())
if num<6:
    print("no")
else:
    cal(num,0)
    for i in sorted(box):
        print(i)