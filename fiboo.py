'''Fibo_V2'''
def fib(num):
    '''Func. fib for faster algorithm for fiboo'''
    fiboo = ((1+(5**0.5))**num-(1-(5**0.5))**num)//(2**num*(5**0.5))
    return int(fiboo)
print(fib(int(input())))
