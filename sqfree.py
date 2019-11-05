"""SqFree by ศิษย์เทพปอง#2"""
def find():
    """Func. find for finding Square Free Number"""
    num = int(input())
    count = 0
    #first loop for running range of number that you input
    #second loop for using number in range(2, num+1) and powered by 2
    for i in range(1, num+1):
        for j in range(2, num+1):
            if j**2 > num:
                break
            if i % j**2 == 0:
                count += 1
                break
    print(num-count)
find()
