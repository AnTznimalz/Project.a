""" GCD LCM """
def main():
    """ Main Func. """
    a = int(input())
    b = int(input())
    print(gcd(a,b))
    print(lcm(a,b))

def gcd(num_1, num_2):
    """ gcd func. """
    if num_2 == 0:
        return num_1
    else:
        return gcd(num_2, num_1 % num_2)
 
""" without gcd """
# def lcm(a,b):
#     """ lcd func. """
#     greater = 0
#     lcm = 0
#     if a > b:
#         greater = a
#     else:
#         greater = b
#     while 1:
#         if((greater % a == 0) and (greater % b == 0)):
#            lcm = greater
#            break
#         greater += 1
#     return lcm

"""With gcd"""
# def lcm(no_1, no_2):
#     """ lcd func. """
#     wow = 0
#     count = 0
#     for _ in range(no_2):
#         wow += no_1
#     while wow != 0:
#         wow -= gcd(no_1, no_2)
#         count += 1
#     return count
def lcm(x, y):
   """ LCM """
   lcm = (x*y)//gcd(x,y)
   return lcm
main()
