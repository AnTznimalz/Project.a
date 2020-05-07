"""00XX: Triangle Area"""
def main():
    """Func. Main"""
    value_1 = float(input())
    value_2 = float(input())
    value_3 = (value_1**2 - value_2**2)**0.5
    area = 0.5 * value_2 * value_3
    print("Area is %.2f" %area)
main()
