"""Kaprekar's Constant"""
def cal(num):
    """Func. cal for calculating Kaprekar's constant"""
    num0 = int(num[0])
    num1 = int(num[1])
    num2 = int(num[2])
    num3 = int(num[3])
    count = 0
    ans = 0
    while ans != 6147:
        if num0 >= num1:
            num0, num1 = num1, num0
        if num0 >= num2:
            num0, num2 = num2, num0
        if num0 >= num3:
            num0, num3 = num3, num0
        if num1 >= num2:
            num1, num2 = num2, num1
        if num1 >= num3:
            num1, num3 = num3, num1
        if num2 >= num3:
            num2, num3 = num3, num2
        count += 1
        ans = int(num3+num2+num1+num0) - int(num0+num1+num2+num3)
    print(count)
cal(input())
