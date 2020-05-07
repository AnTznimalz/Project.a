""" Sort Prepro61 """
def main():
    """ Main Func. """
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    sec = max(num_a, num_b, num_c) + max(num_a, num_b, num_d) + max(num_a, num_d, num_c) + \
        max(num_d, num_b, num_c) - 3*max(num_a, num_b, num_c, num_d)
    third = min(num_a, num_b, num_c) + min(num_a, num_b, num_d) + min(num_a, num_d, num_c) + \
        min(num_d, num_b, num_c) - 3*min(num_a, num_b, num_c, num_d)
    print(max(num_a, num_b, num_c, num_d))
    print(int(sec))
    print(int(third))
    print(min(num_a, num_b, num_c, num_d))
main()
