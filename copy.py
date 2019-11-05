""" GCD_v2 """
def main():
    """ find GCD by Euclid's Law """
    num1, num2 = int(input()), int(input())
    num22, num11 = max(num1, num2), min(num1, num2)
    while num11 != 0:
        num22, num11 = num11, num22%num11
    if num11 == 0:
        print(num22)
main()
