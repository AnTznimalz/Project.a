"""FibonacciRecursionV1"""
def fibo(num=int(input())):
    """Func. fibo for finding Fibonacci"""
    #if num <= 1:
        #return num
    #else:
        #return  fibo(num-1)+fibo(num-2)
    fib = [0,1]
    for _ in range(2, num+1):
        fib.append(fib[-1]+fib[-2])
    return fib[num]
print(fibo())
