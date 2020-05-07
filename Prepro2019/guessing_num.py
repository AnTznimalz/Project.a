"""00xx: Guessing Game"""
def main():
    """Main Func."""
    num = int(input())
    count = 0
    while count != 10:
        ans = int(input())
        if num > ans:
            print("Too Low")
            count += 1
        if num < ans:
            print("Too High")
            count += 1
        if num == ans:
            print("Correct!")
            return
    print("You lose, The answer is %d" %num)
main()
