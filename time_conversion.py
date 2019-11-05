""" Time Conversion """
def time():
    """ Func. time for convert time to 24-hours format """
    msg = input().split(":")
    if 'PM' in msg[-1]:
        if int(msg[0]) % 12 != 0:
            print('0'*(len(msg[0])==1) + str(int(msg[0])%12 +12) + ':' + msg[1] + ':' + msg[-1][:2])
        else:
            print('12' + ':' + msg[1] + ':' + msg[-1][:2])
    else:
        if int(msg[0]) == 12:
            print('00' + ':' + msg[1] + ':' + msg[-1][:2])
        else:
            print((':'.join(msg))[:-2])
time()
