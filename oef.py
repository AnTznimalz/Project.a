"""OddEven Fighting"""
def fighto():
    """Function fighto for finding who the winner is between odd and even"""
    sum_odd = 0
    sum_even = 0
    while True:
        num = int(input())
        if num == 0:
            break
        elif num%2 == 0:
            sum_even += num
        elif num%2 != 0:
            sum_odd += num
    if sum_odd > sum_even:
        print("Odd %d"%sum_odd)
    elif sum_odd < sum_even:
        print("Even %d"%sum_even)
    else:
        print("Draw %d"%sum_odd)
fighto()
