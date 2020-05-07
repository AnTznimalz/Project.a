"""Secret Code"""
def main():
    """Main Func."""
    digit = 1
    num_1 = solve(int(input()), digit)
    digit += 1
    num_2 = solve(int(input()), digit)
    digit += 1
    num_3 = solve(int(input()), digit)
    digit += 1
    num_4 = solve(int(input()), digit)
    digit += 1
    num_5 = solve(int(input()), digit)
    ans = num_1 + num_2 + num_3 + num_4 + num_5
    print("%d+%d+%d+%d+%d = %d" %(num_1, num_2, num_3, num_4, num_5, ans))

def solve(num, digit):
    """Solve Func."""
    num = (num % (10 ** digit))// 10 ** (digit-1)
    return num
main()
