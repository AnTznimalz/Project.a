"""Kaprekar's Constant"""
def cal(num):
    """Func. cal for calculating Kaprekar's constant"""
    count = 0
    while num != "6174":
        if len(num) < 4:
            if len(num) == 1:
                num += "000"
            if len(num) == 2:
                num += "00"
            if len(num) == 3:
                num += "0"
        num0 = num[0]
        num1 = num[1]
        num2 = num[2]
        num3 = num[3]
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
        num = str(int(num3+num2+num1+num0) - int(num0+num1+num2+num3))
    print(count)
cal(input())
