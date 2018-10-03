"""Planc"""
def main():
    """Function"""
    word = input()
    if word == "Ascend":
        order()
    elif word == "Descend":
        dorder()
def order():
    """order func."""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if num1 < num2 < num3:
        print("%.2f, %.2f, %.2f"%(num1, num2, num3))
    elif num1 < num3 < num2:
        print("%.2f, %.2f, %.2f"%(num1, num3, num2))
    elif num2 < num1 < num3:
        print("%.2f, %.2f, %.2f"%(num2, num1, num3))
    elif num2 < num3 < num1:
        print("%.2f, %.2f, %.2f"%(num2, num3, num1))
    elif num3 < num1 < num2:
        print("%.2f, %.2f, %.2f"%(num3, num1, num2))
    elif num3 < num2 < num1:
        print("%.2f, %.2f, %.2f"%(num3, num2, num1))
def dorder():
    """doroder Func."""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if num1 > num2 > num3:
        print("%.2f, %.2f, %.2f"%(num1, num2, num3))
    elif num1 > num3 > num2:
        print("%.2f, %.2f, %.2f"%(num1, num3, num2))
    elif num2 > num1 > num3:
        print("%.2f, %.2f, %.2f"%(num2, num1, num3))
    elif num2 > num3 > num1:
        print("%.2f, %.2f, %.2f"%(num2, num3, num1))
    elif num3 > num1 > num2:
        print("%.2f, %.2f, %.2f"%(num3, num1, num2))
    elif num3 > num2 > num1:
        print("%.2f, %.2f, %.2f"%(num3, num2, num1))
main()
