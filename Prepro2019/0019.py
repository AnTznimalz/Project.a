"""0019: Get Digit"""
def main():
    """Func. main"""
    num = abs(float(input()))
    digit = int(input())
    sub_i = int(num)%(10**(digit))
    sub_f = int(num)%(10**(digit-1))
    want = (sub_i-sub_f)/(10**(digit-1))
    print(int(want))
main()
