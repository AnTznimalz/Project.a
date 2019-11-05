""" Diagonal Matrix"""
def mat():
    """ Func. mat for calculate matrix """
    dim = int(input())
    box = list()
    a, b = 0, 0
    for n in range(dim):
        lst = input().split()
        box.append(lst)
        lst = []
    for i in range(dim):
        a += int(box[i][i])
        b += int(box[i][dim-i-1])
    print(abs(a-b))
mat()
