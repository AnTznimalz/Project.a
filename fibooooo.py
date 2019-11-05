def fib(num):
    '''Func. fib for super speed algorithm for fibo'''
    fib(num) = fib(2*num)+fib(2*num-1)
    fib(2*num) = fib(num-1)**2 + fib(num)**2
    fib(2*num-1) = (2*fib(num+1)+fib(num))*fib(num)
    if num == 0 or num == 1:
        return num
    else:
        return fib(num)
print(fib(int(input())))