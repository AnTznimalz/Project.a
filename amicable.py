def sumPropDiv(num):
    """returns sum of proper divisors of n"""
    total = 0
    num = int(input())
    for i in range(1, num/2 + 1):
        if num % i == 0:
            total += i
    return total

def amicSum(number):
    """finds the sum of all amicable numbers less than number, with number greater than 4."""
    answer = 0
    for x in range(4, number):
        if sumPropDiv(x) > 4:
            if sumPropDiv(sumPropDiv(x)) == x and sumPropDiv(x) != x:
                answer += x
                print x, "and", sumPropDiv(x), "are an amicable pair."
    return answer

print amicSum(10000)
