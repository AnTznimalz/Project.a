""" Kangaroo """
def chk():
    """ Func. chk for checking distance of 2 kangaroos """
    msg = input().split()
    x = int(msg[0])
    vx = int(msg[1])
    y = int(msg[2])
    vy = int(msg[3])
    for _ in range(10000):
        if x+vx == y+vy:
            print('YES')
            return
        x += vx
        y += vy
    print('NO')
chk()
