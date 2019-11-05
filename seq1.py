"""Sequence XI"""
def go(num):
    """Function Go to Run Loop"""
    for i in range(1, num+1):
        for j in range(1, i+1):
            print("%02d" %j, end=" ")
        for k in range(2*num-2*i):
            print("%02d" %j, end=" ")
        for var1 in range(i-1, 0, -1):
            print("%02d" %var1, end=" ")
        print()
    for var2 in range(num-1,0, -1):
        for var3 in range(1, var2+1):
            print("%02d" %var3, end=" ")
        for var4 in range((2*num)-(2*var2)):
            print("%02d" %var3, end=" ")
        for var5 in range(var2-1, 0, -1):
            print("%02d" %var5, end=" ")
        print()
        
go(int(input()))

