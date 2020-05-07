""" Factorial """
# def main():
#     """ Main Func. """
#     a = int(input())
#     ans = 1
#     print(fac(a, ans))
# def fac(a, ans):
#     """ Fac Func. """
#     if a > 1:
#         ans = fac(a-1, ans*a)
#     return ans
# main()
def cal():
    """ Cal Func. """
    ans = 1
    for i in range(2, int(input())+1):
        ans *= i
    print(ans)
cal()


