def fib2(n):
    # return (fib(n), fib(n-1))
    if n ==  0: return (0,  1)
    if n == -1: return (1, -1)
    k, r = divmod(n, 2) # n=2k+r
    u_k, u_km1 = fib2(k)
    u_k_s, u_km1_s = u_k**2, u_km1**2  # Can be improved by parallel calls
    u_2kp1 = 4 * u_k_s - u_km1_s + (-2 if k%2 else 2)
    u_2km1 = u_k_s + u_km1_s
    u_2k   = u_2kp1 - u_2km1
    return (u_2kp1, u_2k) if r else (u_2k, u_2km1)

def fib(n=int(input())):
    k, r = divmod(n, 2) # n=2k+r
    u_k, u_km1 = fib2(k)
    return (2*u_k+u_km1)*(2*u_k-u_km1)+(-2 if k%2 else 2) if r else u_k*(u_k+2*u_km1)
print(fib())
