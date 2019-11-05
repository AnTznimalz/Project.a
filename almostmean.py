"""Median by ศิษย์เทพปอง#2"""
def find():
    """Func. find for finding median"""
    num = int(input())
    box = []
    #Run loop and order number
    for _ in range(num):
        num_a = int(input())
        box.append(num_a)
    box.sort()
    #num1, num2 = index of box
    num1 = box[num//2]
    num2 = box[(num//2)-1]
    #if condition >>> num is even number
    #else condition >>> num is odd number
    if num%2 != 0:
        print("%.1f"%num1)
    else:
        print("%.1f"%((num1+num2)/2))
find()
