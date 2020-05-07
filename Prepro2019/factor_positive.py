"""00xx: Factors of positive number"""
def main():
    """Main Func."""
    num = int(input())
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=" ")
main()
