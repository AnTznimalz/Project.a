"""Factorial"""
import math
def main():
    """Main Func."""
    num_1 = solve(int(input()))
    num_2 = solve(int(input()))
    num_3 = solve(int(input()))
    num_4 = solve(int(input()))
    num_5 = solve(int(input()))
    print(num_1)
    print(num_2)
    print(num_3)
    print(num_4)
    print(num_5)

def solve(num):
    """Solve Func."""
    num = math.factorial(num)
    return num

main()
main()
main()
main()
