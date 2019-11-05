"""All_Prime"""
def sol(num):
    """Func. sol for solving this problem"""
    count = 0
    for j in range(2, num+1):
        if all(j%i != 0 for i in range(2, j)):
            count += 1
    print(count)
sol(int(input()))
