""" Staircase """
def draw():
    """ Func. draw for drawing staircase """
    num = int(input())
    for i in range(1, num+1):
        print(" "*(num-i),end="")
        print("#"*i)
draw()
