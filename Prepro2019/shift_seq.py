""" Shift Sequence """
def main():
    """ Main Func. """
    num = int(input())
    for i in range(1, num+1):
        for j in range(i, num+1):
            print(j, end="")
        for k in range(1, i):
            print(k, end="")
        print()
main()


# """ Shift Sequence """
# def main(num):
#     """ print Sequence """
#     for i in range(num):
#         for j in range(num):
#             print((i+j)%num+1, end="")
#         print()
# main(int(input()))