"""00xx: Sandglass"""
def main():
    """Main Func."""
    num = int(input())
    if num % 2 == 0:
        print("Errrrrrrrrrrrrr")
    else:
        #triangle down
        count = 1
        for i in range(num, 0, -2):
            if i < num:
                print(" "*count + "*"*i)
                count += 1
            else:
                print("*"*i)
        #triangle up
        count = num//2 - 1
        for i in range(3, num+1, 2):
            if i < num and i != 1:
                print(" "*count + "*"*i)
                count -= 1
            else:
                print("*"*i)
main()
