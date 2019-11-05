f = lambda x: x+5
print(f(int(input())))

fib = [0,1,1,2,3,5]
res = filter(lambda x: x%2==0, fib)
print(res)

r = reduce(lambda x,y: x+y [3,4,5,6,7,8])