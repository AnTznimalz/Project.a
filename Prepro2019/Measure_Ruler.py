"""00XX: Measure Ruler"""
def main():
    """Func. Main"""
    value_1 = check()
    value_2 = check()
    print("%.2f ruler(s) or %.2f cm" %(max(value_1, value_2), max(value_1, value_2)*30))
def check():
    """Func. check"""
    thing_1 = float(input())
    thing_2 = float(input())
    thing_3 = float(input())
    thing_4 = float(input())
    thing_5 = float(input())
    return max(thing_1, thing_2, thing_3, thing_4, thing_5)

main()
