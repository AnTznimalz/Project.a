"""Sequence XII"""
def run(num):
    """Function run for running Loop"""
    for i in range(1-num, num):
        for j in range(1-num, num):
            print("%02d" %(num-abs((abs(i)-abs(j)))), end=" ")
        print()
run(int(input()))
