""" Sleep Enough? """
 
def result():
    """ Result of Sleep """
    s_h = int(input())
    s_m = int(input())
    w_h = int(input())
    w_m = int(input())
    #plus 7hrs and 30mins
    s_m += 450
    s_h += s_m//60
    s_m = s_m % 60
    if s_h > 23:
        s_h -= 24
    if (w_h >= s_h and w_m >= s_m) and (w_h - s_h <= 3):
        print("Sleep enough!")
    elif (s_h - w_h > 10) and w_m >= s_m:
        print("Sleep enough!")
    else:
        print("P'Guy have to wake up at %02d:%02d" %(s_h, s_m)) 
result()
