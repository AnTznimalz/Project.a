"""Perfect Number""" 
def divisor(num):
    """Func. divisor for finding sum of divisor""" 
    wow = 1
    total = 0
    ans = 0
    while wow != num: 
        if num % wow == 0: 
            total += wow
        if wow == total:
            ans += wow
        wow = wow + 1
    print(ans)
divisor(int(input()))
