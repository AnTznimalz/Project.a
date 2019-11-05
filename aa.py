"""Sequence XI"""
def run():
    """Function Run For Running Loop"""
    num = int(input())
    for i in range(1, num+1):
        for j in range(i):
            print("%02d" %(j+1), end=" ")
            wow = j
        for _ in range(2*num-2*i):
            print("%02d" %(wow+1), end=" ")
        for dog in range(i-1, 0, -1):
            print("%02d" %dog, end=" ")
        print()
    for i in range(num-1, 0, -1):
        for j in range(i):
            print("%02d" %(j+1), end=" ")
            wow = j
        for _ in range(2*num-2*i):
            print("%02d" %(wow+1), end=" ")
        for dog in range(i-1, 0, -1):
            print("%02d" %dog, end=" ")
        print()
run()
