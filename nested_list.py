""" Nested Lists """
def main():
    """ Main Func. """
    a, b = [], []
    c = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        a.append(name)
        a.append(score)
        b.append(a)
        a = []
    b.sort(key=lambda x: x[1])
    print(b)
    for i in range(len(b)):
        c.append(b[i][1])
    print(c)
    # while len(b) > 3:
    #         b.pop()
    # print(b)
    # if b[0][1] < b[1][1] < b[2][1]:
    #     print(b[1][1])
        
    # if b[0][1] != b[1][1]:
    #     print(b[0][0])
    # else:
    #     b.sort(key=lambda x: x[0])
    #     print(b[0][0])
    #     print(b[1][0])
main()
