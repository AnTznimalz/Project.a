"""Are they equal?"""
def main():
    """Main Func."""
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    print("%d and %d are equal." %(num_1, num_2))
    print("This sentence is %s." %(num_1 == num_2))
    print("%d and %d are equal." %(num_2, num_3))
    print("This sentence is %s." %(num_3 == num_2))
    print("%d and %d are equal." %(num_1, num_3))
    print("This sentence is %s." %(num_1 == num_3))
main()
