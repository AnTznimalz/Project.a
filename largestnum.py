"""Largest Number"""
def order(num1, num2, num3):
    """Func. order for making the largest number"""
    num123 = int(num1 + num2 + num3)
    num132 = int(num1 + num3 + num2)
    num213 = int(num2 + num1 + num3)
    num231 = int(num2 + num3 + num1)
    num312 = int(num3 + num1 + num2)
    num321 = int(num3 + num2 + num1)
    if num123 >= num132 and num123 >= num213 and num123 >= num231 \
    and num123 >= num312 and num123 >= num321:
        print(num123)
    elif num132 >= num123 and num132 >= num213 and num132 >= num231 \
    and num132 >= num312 and num132 >= num321:
        print(num132)
    elif num213 >= num132 and num213 >= num123 and num213 >= num231 \
    and num213 >= num312 and num213 >= num321:
        print(num213)
    elif num231 >= num132 and num231 >= num213 and num231 >= num123 \
    and num231 >= num312 and num231 >= num321:
        print(num231)
    elif num312 >= num132 and num312 >= num213 and num312 >= num231 \
    and num312 >= num123 and num312 >= num321:
        print(num312)
    else:
        print(num321)
order(input(), input(), input())
