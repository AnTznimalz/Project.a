"""(loop) Factorial V2"""
def main():
    """Main Func."""
    check = 0
    while check != 20:
        num = int(input())
        ans = 1
        for i in range(1, num+1):
            ans *= i
        print(ans)
        check += 1
main()
