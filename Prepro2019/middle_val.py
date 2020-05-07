"""Middle Value"""
def main():
    """Main Func."""
    num_1, num_2, num_3 = int(input()), int(input()), int(input())
    ans = (max(num_1, num_2) + max(num_1, num_3) + max(num_2, num_3)) - \
        (2* max(num_1, num_2, num_3))
    print(ans)
main()
