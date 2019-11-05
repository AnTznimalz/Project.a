'''Fibo_V2 by ศิษย์เทพปอง#2'''
def fib(num):
    '''
    Func. fib to run super speed fibo
    reference from
    https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series
    '''
    fibs = {0: 0, 1: 1}
    if num in fibs:
        return fibs[num]
    if num % 2 == 0:
        fibs[num] = ((2 * fib((num / 2) - 1)) + fib(num / 2)) * fib(num / 2)
        return fibs[num]
    else:
        fibs[num] = (fib((num - 1) / 2) ** 2) + (fib((num+1) / 2) ** 2)
        return fibs[num]
print(fib(int(input())))
