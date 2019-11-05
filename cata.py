"""FibonacciRecursionV1"""
def cata(num=int(input())):
    """Func. fibo for finding Fibonacci"""
    if num == 1:
        return 1
    else:
        return  (4*num+2)/(num+2) * cata(num)
print(cata())
