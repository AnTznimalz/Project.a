"""00XX: Blink"""
def main():
    """main func."""
    freq_1 = int(input())
    freq_2 = int(input())
    time = int(input())
    if time % lcm(freq_1, freq_2) == 0 and lcm(freq_1, freq_2) != 1:
        print("yes")
    else:
        print("no")
def gcd(num_1, num_2):
    """gcd func."""
    if num_2 == 0:
        return num_1
    else:
        return gcd(num_2, num_1 % num_2)
def lcm(no_1, no_2):
    """lcd func."""
    wow = 0
    count = 0
    for _ in range(no_2):
        wow += no_1
    while wow != 0:
        wow -= gcd(no_1, no_2)
        count += 1
    return count

main()
