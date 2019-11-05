"""isPrime_large by ศิษย์เทพปอง#2"""
def say():
    """Func. say for saying Yes or No for the prime number"""
    num = int(input())
    state = "YES"
    #this loop for checking prime number is not state>>>'NO'
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            state = "NO"
            break
    #if condition for trapping num == '1' or '0'
    if num == 1 or num == 0:
        state = "NO"
    print(state)
say()
