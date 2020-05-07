""" Def Pyramid """
def main(num):
    """ Main Func. """
    for i in range((num+1)*2):
        for j in range(-((num*2)+1), (num*2)+2):
            #Outer shield
            if (i -abs(j))%2 != 0 or abs(j) > i:
                print(" ", end="")
            else:
                print(num-((i-abs(j))//2), end="")
        print()
main(int(input()))
