"""Key_Midterm_2014"""
def key(num):
    """Func. key for finding secret 4 digits's secret"""
    num = str(num)  #num;int >> str:for seperating digit to get sum
    total = 0
    total = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])\
    + int(num[4]) + int(num[5]) + int(num[6]) + int(num[7])\
    + int(num[8]) + int(num[9]) + int(num[10]) + int(num[11])\
    + int(num[12])
    num = int(num)  #num;str >> int:for cutting last 3 digits of num
    tdeci = (num%1000)*10
    final = total+tdeci
    final = str(final)
    if len(final) > 4:
        print(final[-4]+final[-3]+final[-2]+final[-1])
    elif len(final) < 4:
        final = int(final)
        final += 1000
        print(final)
    else:
        print(final)

key(int(input()))
