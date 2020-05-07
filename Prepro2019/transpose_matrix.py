#Just for one digit number
# """ Transpose of Matrix """
# def trans():
#     """ Trans Func. """
#     row = int(input())
#     col = int(input())
#     a = []
#     b = ""
#     for i in range(row):
#         for j in range(col):
#             b += (input())
#         a.append(b)
#         b = ""
#     print(b)
#     print(a)
#     print("Matrix A:")
#     for i in range(row):
#         for j in range(col):
#             print(a[i][j], end=" ")
#         print()
#     print()
#     print("Transpose of Matrix A:")
#     for i in range(row):
#         for j in range(col):
#             print(a[j][i], end=" ")
#         print()
# trans()
""" Transpose of Matrix """
def trans():
    """ Trans Func. """
    row = int(input())
    col = int(input())
    a_l = []
    b_l = []
    for i in range(row):
        for j in range(col):
            b_l.append(int(input()))
        a_l.append(b_l)
        b_l = []
    print("Matrix A:")
    for i in range(row):
        for j in range(col):
            print(a_l[i][j], end=" ")
        print()
    print()
    print("Transpose of Matrix A:")
    for i in range(col):
        for j in range(row):
            print(a_l[j][i], end=" ")
        print()
trans()
